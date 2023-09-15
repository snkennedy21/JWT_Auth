import { usePartiallyProtectedEndpointQuery } from "./store/mainAPI";

export default function PartiallyProtectedEndpoint() {
  const { data, isLoading } = usePartiallyProtectedEndpointQuery();

  if (isLoading) return <div>Is Loading</div>;
  return <div>{data.user}</div>;
}
