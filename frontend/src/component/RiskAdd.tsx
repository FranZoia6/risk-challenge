import React, { useState } from "react";
import { fetchPost } from "../utils/request";
import { toast } from "react-toastify";

interface RiskItem {
  id: string;
  cod: string;
  impact: string;
  title: string;
  description: string;
  resolved: boolean;
}

type Props = {
  token: string;
  setRiskList: React.Dispatch<React.SetStateAction<RiskItem[]>>;
};

function RiskAdd({ token, setRiskList }: Props) {
  const url = "http://localhost:5000/risk/add";

  const [title, setTitle] = useState("");
  const [cod, setCod] = useState("");
  const [description, setDescription] = useState("");
  const [impact, setImpact] = useState("High");
  const [resolved, setResolved] = useState(false);
  const [popUp, setPopUp] = useState(false);

  // Función que maneja la adición de un nuevo riesgo.
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const risk = {
      title,
      description,
      cod,
      impact,
      resolved,
    };

    const request = { risk };

    const data = await fetchPost(url, request, token);
    console.log(data);
    if (data.status) {
      const newRisk = { ...risk, id: data.data?.id };
      setRiskList((prevList) => [...prevList, newRisk]);
      toast.success("Riesgo agregado");
    } else {
      toast.error("Error al agregar riesgo");
    }
  };

  return (
    <>
      <button
        className="btn btn-primary"
        onClick={() => {
          setPopUp(true);
        }}
      >
        Agregar
      </button>
      {popUp && (
        <div className="modal-container">
          <h2>Agregar Riesgo</h2>
          <form
            onSubmit={handleSubmit}
            className="p-4 border rounded shadow bg-white"
          >
            <label className="form-label">Codigo:</label>
            <input
              type="text"
              value={cod}
              onChange={(e) => setCod(e.target.value)}
              className="form-control"
              required
            />
            <label className="form-label">Título:</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="form-control"
              required
            />

            <label className="form-label">Descripción:</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="form-control"
              required
            />

            <label className="form-label">Impacto:</label>
            <select
              value={impact}
              onChange={(e) => setImpact(e.target.value)}
              className="form-control"
              required
            >
              <option value="High">High</option>
              <option value="Medium">Medium</option>
              <option value="Low">Low</option>
            </select>

            <label className="form-label">
              Resuelto:
              <input
                type="checkbox"
                checked={resolved}
                onChange={(e) => setResolved(e.target.checked)}
              />
            </label>

            <div className="d-flex justify-content-between mt-3">
              <button type="submit" className="btn btn-primary">
                Agregar
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => {
                  setPopUp(false);
                }}
              >
                Cancelar
              </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
}

export default RiskAdd;
