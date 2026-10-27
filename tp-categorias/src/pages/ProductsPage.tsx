import React from "react";

const ProductsPage: React.FC = () => {
  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Catálogo de Productos</h1>
        <p className="text-gray-600 text-base max-w-2xl mb-6">
          Gestión del catálogo de productos y relación muchos-a-muchos con categorías.
        </p>
        <div className="p-4 bg-indigo-50 border border-indigo-100 rounded-xl">
          <p className="text-sm text-indigo-900 font-medium">
            💡 El CRUD de Productos y la relación muchos-a-muchos se administran desde el backend y
            se demuestran con el archivo <code className="font-mono font-bold">productos.http</code>{" "}
            mediante REST Client.
          </p>
        </div>
      </div>
    </main>
  );
};

export default ProductsPage;