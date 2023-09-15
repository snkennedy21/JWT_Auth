import { useUnprotectedEndpointQuery } from "./store/mainAPI";

export default function UnprotectedEndpoint() {
  const { data, isLoading } = useUnprotectedEndpointQuery();
  console.log(data);

  if (isLoading) return <div>Is Loading</div>;

  return <div>{data.value}</div>;
}
