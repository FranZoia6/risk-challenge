import React, { useState } from "react";
import { fetchPut } from "../utils/request";

interface RiskItem {
  id: string;
  cod: string;
  impact: string;
  title: string;
  description: string;
  resolved: boolean;
}

type Props = {
  riskItem: RiskItem;
  onClose: () => void;
  token: string;
  setRiskList: React.Dispatch<React.SetStateAction<RiskItem[]>>;
};

function RiskUpdate({
  riskItem,
  onClose,
  token,
  setRiskList,
}: Props) {
  const url = "http://localhost:5000/risk/";

  const [title, setTitle] = useState(riskItem.title);
  const [description, setDescription] = useState(riskItem.description);
  const [impact, setImpact] = useState(riskItem.impact);
  const [resolved, setResolved] = useState(riskItem.resolved);

   // Realizar la solicitud PUT para actualizar el riesgo
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const updatedRisk = {
      id: riskItem.id,
      title,
      description,
      cod: riskItem.cod,
      impact,
      resolved,
    };

    const data = await fetchPut(url, updatedRisk, token);

    if (data.status) {
      setRiskList((prevRiskList: RiskItem[]) =>
        prevRiskList.map((item) =>
          item.id === updatedRisk.id ? { ...item, ...updatedRisk } : item
        )
      );
    }
    onClose();
  };

  return (
    <div className="modal-container">
      <h2>Actualizar Riesgo</h2>
      <form
        onSubmit={handleSubmit}
        className="p-4 border rounded shadow bg-white"
      >
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
            Actualizar
          </button>
          <button type="button" className="btn btn-secondary" onClick={onClose}>
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
}

export default RiskUpdate;
