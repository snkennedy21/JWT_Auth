import { usePartiallyProtectedEndpointQuery } from "./store/mainAPI";

export default function PartiallyProtectedEndpoint() {
  const { data, isLoading } = usePartiallyProtectedEndpointQuery();

  if (isLoading) return <div>Is Loading</div>;
  return (
    <>
      <div>
        This page is partially protected by authentication requirements. Anyone
        can access the page and the API endpoint associated with it, but you can
        make decisions on the backend based on the users authentication status.
      </div>
      <p>
        Take a look at what's going on under the hood to better understand why
      </p>

      <div>Response From API</div>
      <div>{data.user}</div>
    </>
  );
}
