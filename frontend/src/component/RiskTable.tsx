import { useState } from "react";
import RiskUpdate from "./RiskUpdate";

interface RiskItem {
  id: string;
  cod: string;
  impact: string;
  title: string;
  description: string;
  resolved: boolean;
}

const impactColors: { [key: string]: string } = {
  High: "text-danger",
  Medium: "text-warning",
  Low: "text-secondary",
};

type Props = {
  riskList: RiskItem[];
  token: string;
};

const RiskTable = ({ riskList, token }: Props) => {
  const [page, setPage] = useState(1);
  const [selectedRisk, setSelectedRisk] = useState<RiskItem | null>(null);
  const itemsPerPage = 10;

  const totalPage = Math.ceil(riskList.length / itemsPerPage);
  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedRisks = riskList.slice(startIndex, endIndex);
  console.log(riskList);
  return (
    <>
      <table className="table table-bordered table-hover">
        <thead>
          <tr>
            <th>Título</th>
            <th>Código</th>
            <th>Impacto</th>
            <th>Descripción</th>
            <th>Resuelto</th>
            <th>Actualizar</th>
          </tr>
        </thead>
        <tbody>
          {paginatedRisks.map((riskItem) => (
            <tr key={riskItem.id}>
              <td>{riskItem.title}</td>
              <td>{riskItem.cod}</td>
              <td>
                <span
                  className={impactColors[riskItem.impact] || "text-secondary"}
                >
                  {riskItem.impact}
                </span>
              </td>
              <td>{riskItem.description}</td>
              <td>
                {riskItem.resolved ? (
                  <span className="text-success fw-bold">Sí</span>
                ) : (
                  <span className="text-danger fw-bold">No</span>
                )}
              </td>
              <td>
                <button
                  className="btn btn-primary"
                  onClick={() => setSelectedRisk(riskItem)}
                >
                  Actualizar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {totalPage > 1 && (
        <div style={{ margin: "5px", textAlign: "center" }}>
          <button
            disabled={page === 1}
            onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
          >
            ⬅️
          </button>
          {Array.from({ length: totalPage }, (_, index) => (
            <button
              key={index}
              onClick={() => setPage(index + 1)}
              disabled={page === index + 1}
              style={{
                fontWeight: page === index + 1 ? "bold" : "normal",
                margin: "5px",
              }}
            >
              {index + 1}
            </button>
          ))}
          <button
            disabled={page === totalPage}
            onClick={() => setPage((prev) => Math.min(prev + 1, totalPage))}
          >
            ➡️
          </button>
        </div>
      )}

      {selectedRisk && (
        <div className="modal-overlay position-fixed top-0 start-0 w-100 h-100 bg-dark bg-opacity-50 d-flex justify-content-center align-items-center">
          <div className="modal-dialog">
            <div className="modal-content">
              <button
                className="btn-close"
                onClick={() => setSelectedRisk(null)}
                aria-label="Cerrar"
              />
              <RiskUpdate
                riskItem={selectedRisk}
                onClose={() => setSelectedRisk(null)}
                token={token}
              />
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default RiskTable;
