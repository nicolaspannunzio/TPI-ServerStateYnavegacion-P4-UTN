import React, { useState } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import {
  getCategorias,
  createCategoria,
  updateCategoria,
  deleteCategoria,
} from "../services/categoria";
import type { Categoria, CategoriaCreate } from "../types/categoria";
import CategoriaList from "../components/CategoriaList";
import CategoriaModal from "../components/CategoriaModal";

const CategoriasPage: React.FC = () => {
  const queryClient = useQueryClient();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingCategoria, setEditingCategoria] = useState<Categoria | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);
  const [mutationError, setMutationError] = useState<string | null>(null);

  const {
    data: categorias = [],
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["categorias"],
    queryFn: getCategorias,
  });

  const createMutation = useMutation({
    mutationFn: createCategoria,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ["categorias"] });
      setMutationError(null);
      setIsModalOpen(false);
    },
    onError: (error) => setMutationError(error instanceof Error ? error.message : "Error al crear categoría"),
  });

  const updateMutation = useMutation({
    mutationFn: updateCategoria,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ["categorias"] });
      setMutationError(null);
      setIsModalOpen(false);
      setEditingCategoria(null);
    },
    onError: (error) => setMutationError(error instanceof Error ? error.message : "Error al actualizar categoría"),
  });

  const deleteMutation = useMutation({
    mutationFn: deleteCategoria,
    onMutate: (id) => {
      setDeletingId(id);
    },
    onSettled: () => {
      setDeletingId(null);
    },
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ["categorias"] });
      setMutationError(null);
    },
    onError: (error) => setMutationError(error instanceof Error ? error.message : "Error al eliminar categoría"),
  });

  const handleOpenCreateModal = () => {
    setMutationError(null);
    setEditingCategoria(null);
    setIsModalOpen(true);
  };

  const handleOpenEditModal = (cat: Categoria) => {
    setMutationError(null);
    setEditingCategoria(cat);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setMutationError(null);
    setIsModalOpen(false);
    setEditingCategoria(null);
  };

  const handleModalSubmit = (data: CategoriaCreate) => {
    setMutationError(null);
    if (editingCategoria) {
      updateMutation.mutate({ id: editingCategoria.id, data });
    } else {
      createMutation.mutate(data);
    }
  };

  const handleDelete = (id: number) => {
    if (window.confirm("¿Seguro que deseas eliminar esta categoría?")) {
      deleteMutation.mutate(id);
    }
  };

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-gray-900">Categorías</h1>
          <p className="text-sm text-gray-500 mt-1">
            Administración de categorías del catálogo (TanStack Query + FastAPI)
          </p>
        </div>
        <button
          onClick={handleOpenCreateModal}
          className="inline-flex items-center gap-2 px-4 py-2 text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg shadow-sm transition"
        >
          <span>+</span> Añadir Categoría
        </button>
      </div>

      {mutationError && (
        <div role="alert" className="mb-4 rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-700">
          {mutationError}
        </div>
      )}

      {isLoading && (
        <div className="flex justify-center items-center py-20">
          <p className="text-gray-500 font-medium">Cargando categorías...</p>
        </div>
      )}

      {isError && (
        <div className="p-4 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-sm">
          {error instanceof Error ? error.message : "Error al conectar con el servidor"}
        </div>
      )}

      {!isLoading && !isError && (
        <CategoriaList
          categorias={categorias}
          onEdit={handleOpenEditModal}
          onDelete={handleDelete}
          deletingId={deletingId}
        />
      )}

      <CategoriaModal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        onSubmit={handleModalSubmit}
        initialData={editingCategoria}
        isLoading={createMutation.isPending || updateMutation.isPending}
        error={mutationError}
      />
    </main>
  );
};

export default CategoriasPage;