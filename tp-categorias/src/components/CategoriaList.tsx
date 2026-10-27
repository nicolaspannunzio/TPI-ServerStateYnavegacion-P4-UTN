import React from "react";
import type { Categoria } from "../types/categoria";
import CategoriaCard from "./CategoriaCard";

interface CategoriaListProps {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
  deletingId?: number | null;
}

const CategoriaList: React.FC<CategoriaListProps> = ({
  categorias,
  onEdit,
  onDelete,
  deletingId,
}) => {
  if (categorias.length === 0) {
    return (
      <div className="text-center py-12 bg-white rounded-xl shadow-sm border border-gray-100">
        <p className="text-gray-500 text-base">No hay categorías registradas en el sistema.</p>
      </div>
    );
  }

  return (
    <div className="overflow-hidden bg-white shadow-sm rounded-xl border border-gray-100">
      <table className="min-w-full divide-y divide-gray-200 text-left">
        <thead className="bg-gray-50">
          <tr>
            <th className="py-3.5 px-6 text-xs font-semibold uppercase tracking-wider text-gray-500">
              Número
            </th>
            <th className="py-3.5 px-6 text-xs font-semibold uppercase tracking-wider text-gray-500">
              Nombre
            </th>
            <th className="py-3.5 px-6 text-xs font-semibold uppercase tracking-wider text-gray-500">
              Descripción
            </th>
            <th className="py-3.5 px-6 text-xs font-semibold uppercase tracking-wider text-gray-500 text-right">
              Acciones
            </th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100">
          {categorias.map((cat) => (
            <CategoriaCard
              key={cat.id}
              categoria={cat}
              onEdit={onEdit}
              onDelete={onDelete}
              isDeleting={deletingId === cat.id}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CategoriaList;