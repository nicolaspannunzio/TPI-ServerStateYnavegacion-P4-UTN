import type { Categoria, CategoriaCreate, CategoriaUpdate } from "../types/categoria";

const API_URL = (import.meta.env.VITE_API_URL ?? "http://localhost:8000").replace(/\/$/, "");

async function apiError(response: Response, fallback: string): Promise<Error> {
  let detail = fallback;
  try {
    const body: unknown = await response.json();
    if ( body && typeof body === "object" && "detail" in body) {
      const value = (body as { detail?: unknown }).detail;
      detail = typeof value === "string" ? value : JSON.stringify(value);
    }
  } catch { /* La respuesta puede no incluir JSON. */ }
  return new Error(`${detail} (HTTP ${response.status})`);
}

export async function getCategorias(): Promise<Categoria[]> {
  const response = await fetch(`${API_URL}/categorias/`);
  if (!response.ok) throw await apiError(response, "No se pudieron obtener las categorías");
  return response.json() as Promise<Categoria[]>;
}

export async function createCategoria(data: CategoriaCreate): Promise<Categoria> {
  const response = await fetch(`${API_URL}/categorias/`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data),
  });
  if (!response.ok) throw await apiError(response, "No se pudo crear la categoría");
  return response.json() as Promise<Categoria>;
}

export async function updateCategoria({ id, data }: { id: number; data: CategoriaUpdate }): Promise<Categoria> {
  const response = await fetch(`${API_URL}/categorias/${id}`, {
    method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data),
  });
  if (!response.ok) throw await apiError(response, "No se pudo actualizar la categoría");
  return response.json() as Promise<Categoria>;
}

export async function deleteCategoria(id: number): Promise<void> {
  const response = await fetch(`${API_URL}/categorias/${id}`, { method: "DELETE" });
  if (!response.ok) throw await apiError(response, "No se pudo eliminar la categoría");
}
