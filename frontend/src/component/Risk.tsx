interface RiskItem {
  id: string;
  impact: string;
  title: string;
  description: string;
}

type Props = {
  risk: RiskItem;
};

const Risk = ({ risk }: Props) => {
  return (
    <div className="card">
      <h5 className="card-header">{risk.title}</h5>
      <div className="card-body">
        <p className="card-text">
          <strong>Impact:</strong> {risk.impact}
        </p>
        <p className="card-text">{risk.description}</p>
      </div>
    </div>
  );
};

export default Risk;
