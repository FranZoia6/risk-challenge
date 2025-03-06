import { PieChart, Pie, Cell, Legend, Tooltip } from "recharts";

interface RiskItem {
  id: string;
  cod: string;
  impact: string;
  title: string;
  description: string;
  resolved: boolean;

}

type Props = { riskList: RiskItem[] };

const RiskMetrics = ({ riskList }: Props) => {
  const resolvedCount = riskList.filter((risk) => risk.resolved).length;
  const unresolvedCount = riskList.length - resolvedCount;

  const impactCount = riskList.reduce((acc, risk) => {
    acc[risk.impact] = (acc[risk.impact] || 0) + 1;
    return acc;
  }, {} as { [key: string]: number });

  const resolvedData = [
    { name: "Resuelto", value: resolvedCount },
    { name: "No Resuelto", value: unresolvedCount },
  ];

  const impactData = Object.entries(impactCount).map(([impact, count]) => ({
    name: impact,
    value: count,
  }));

  return (
    <div>
      <h3>Métricas de Riesgo</h3>

      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          marginBottom: "30px",
        }}
      >
        <div style={{ flex: 1, textAlign: "center" }}>
          <h4>Riesgos Resueltos vs No Resueltos</h4>
          <PieChart width={250} height={250}>
            <Pie
              data={resolvedData}
              dataKey="value"
              nameKey="name"
              outerRadius={100}
              fill="#8884d8"
              label
            >
              <Cell name="Resuelto" fill="#82ca9d" />
              <Cell name="No Resuelto" fill="#ff6f61" />
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </div>

        <div style={{ flex: 1, textAlign: "center" }}>
          <h4>Distribución de Impacto</h4>
          <PieChart width={250} height={250}>
            <Pie
              data={impactData}
              dataKey="value"
              nameKey="name"
              outerRadius={100}
              fill="#8884d8"
              label
            >
              {impactData.map((_, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={["#82ca9d", "#ff6f61", "#8884d8"][index % 3]}
                />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </div>
      </div>
    </div>
  );
};

export default RiskMetrics;
