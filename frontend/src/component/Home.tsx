import { useState, useEffect } from "react";
import RiskMetrics from "./RiskMetrics";
import { fetchPost, useFetchGet } from "../utils/request";
import { toast } from "react-toastify";
import RiskTable from "./RiskTable";

interface RiskItem {
  id: string;
  cod: string;
  impact: string;
  title: string;
  description: string;
  resolved: boolean;
}

interface RiskResponse {
  risks: RiskItem[];
}

type Props = {
  token: string;
  user: {};
  setToken: (token: string) => void;
  setAuthenticated: (auth: boolean) => void;
};

function Home({ setToken, token, user, setAuthenticated }: Props) {
  const [text, setText] = useState("");
  const [riskList, setRiskList] = useState<RiskItem[]>([]);
  const url = "http://localhost:5000/risk/";
 const { data } = useFetchGet<RiskResponse>(url, token);
  console.log(data);

  const [isFirstFetch, setIsFirstFetch] = useState(true);

  useEffect(() => {
    if (isFirstFetch && data?.risks) {
      const formattedRisks = data.risks.map((risk: any) => ({
        ...risk,
        resolved: risk.resolved === 1,
      }));
      setRiskList(formattedRisks);
      setIsFirstFetch(false);
    }
  }, [data, isFirstFetch]);

  const handleSendRisk = async (text: string) => {
    const request = { text };
    try {
      const response = await fetchPost(url, request, token);
      const urlToken = "http://127.0.0.1:5000/auth/login";
      setAuthenticated(response.status);

      if (response.status) {
        const responseToken = await fetchPost(urlToken, user);
        setToken(responseToken.data.token);
        setRiskList(response.data.risks || []);
      }
    } catch (error) {
      toast.error("Error");
    }
  };

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
      {riskList.length > 0 ? (
        <div>
          <RiskMetrics riskList={riskList} />
          <RiskTable riskList={riskList} token= {token}/>
        </div>
      ) : (
        <p>Sin resultados</p>
      )}
    </>
  );
}

export default Home;
