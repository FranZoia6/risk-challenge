import React, { useState } from "react";
import { fetchPost } from "../utils/request";
import Risk from "./Risk";

interface RiskItem {
  id: string;
  impact: string;
  title: string;
  description: string;
}

type Props = {
  setToken: (token: string) => void;
  token: string;
};

function Home({ setToken, token }: Props) {
  const [text, setText] = useState("");
  const [page, setPage] = useState(1);
  const [riskList, setRiskList] = useState<RiskItem[]>([]);
  const itemsPerPage = 10;
  const url = "http://localhost:5000/risk/";

  const handleSendRisk = async (text: string) => {
    const request = { text };
    console.log(token);
    const response = await fetchPost(url, request, token);
    setRiskList(response.data.risks || []);
    setPage(1);
  };

  const totalPage = Math.ceil(riskList.length / itemsPerPage);

  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedRisks = riskList.slice(startIndex, endIndex);

  return (
    <>
      <div style={{ margin: "5px" }}>
        <h1>Risk - Challenge</h1>
        <textarea
          className="form-control"
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSendRisk(text);
            }
          }}
          placeholder="Escribe tu mensaje y presiona Enter"
        />
      </div>

      <div>
        {paginatedRisks.length > 0 &&
          paginatedRisks.map((riskItem) => (
            <Risk key={riskItem.id} risk={riskItem} />
          ))}
      </div>
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
    </>
  );
}

export default Home;
