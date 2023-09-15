import { useProtectedEndpointQuery } from "./store/mainAPI";

export default function ProtectedEndpoint() {
  const { data } = useProtectedEndpointQuery();

  console.log(data);

  return <div>{data.value}</div>;
}
