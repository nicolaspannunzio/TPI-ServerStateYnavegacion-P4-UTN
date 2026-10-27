import React from "react";
import type { Categoria } from "../types/categoria";

interface CategoriaCardProps {
  categoria: Categoria;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
  isDeleting?: boolean;
}

const CategoriaCard: React.FC<CategoriaCardProps> = ({
  categoria,
  onEdit,
  onDelete,
  isDeleting = false,
}) => {
  return (
    <tr className="border-b border-gray-100 hover:bg-gray-50 transition duration-150">
      <td className="py-4 px-6 text-sm text-gray-500 font-medium">{categoria.id}</td>
      <td className="py-4 px-6 text-sm font-semibold text-gray-900">{categoria.nombre}</td>
      <td className="py-4 px-6 text-sm text-gray-600 max-w-md truncate">{categoria.descripcion}</td>
      <td className="py-4 px-6 text-sm text-right space-x-2 whitespace-nowrap">
        <button
          onClick={() => onEdit(categoria)}
          className="px-3 py-1.5 text-xs font-semibold text-indigo-700 bg-indigo-50 hover:bg-indigo-100 rounded-lg transition"
        >
          Editar
        </button>
        <button
          onClick={() => onDelete(categoria.id)}
          disabled={isDeleting}
          className="px-3 py-1.5 text-xs font-semibold text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-lg transition disabled:opacity-50"
        >
          {isDeleting ? "Borrando..." : "Eliminar"}
        </button>
      </td>
    </tr>
  );
};

export default CategoriaCard;