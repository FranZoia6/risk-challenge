import { useState, useEffect } from "react";

export function useFetchGet<T>(
  url: string,
  token: string
): { data: T | undefined; loading: boolean; error: string | null } {
  const [data, setData] = useState<T | undefined>(undefined); // Cambiar el tipo de 'data' a 'T | undefined'
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  useEffect(() => {
    const request = {
      method: "GET",
      headers,
    };

    setLoading(true);
    setError(null); // Reset error on every request

    fetch(url, request)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        return response.json();
      })
      .then((responseData) => {
        setData(responseData); // Asignar el tipo genérico a 'data'
      })
      .catch((error) => {
        setError(error.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [url, token]); // Dependencias actualizadas

  return { data, loading, error };
}

export async function fetchPost(
  url: string,
  data: Record<string, unknown>,
  token?: string
) {
  try {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
    };

    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(url, {
      method: "POST",
      headers,
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const responseData = await response.json();
    return { status: true, data: responseData };
  } catch (error) {
    return { status: false, data: null };
  }
}


export async function fetchPut(
  url: string,
  data: Record<string, unknown>,
  token?: string
) {
  try {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
    };

    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(url, {
      method: "PUT",
      headers,
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const responseData = await response.json();
    return { status: true, data: responseData };
  } catch (error) {
    return { status: false, data: null };
  }
}

