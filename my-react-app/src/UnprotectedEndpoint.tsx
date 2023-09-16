import { useUnprotectedEndpointQuery } from "./store/mainAPI";

export default function UnprotectedEndpoint() {
  const { data, isLoading } = useUnprotectedEndpointQuery();
  console.log(data);

  if (isLoading) return <div>Is Loading</div>;

  return (
    <>
      <div>
        This page is not protected by authentication requirements. Anyone can
        access the page and the API endpoint associated with it.
      </div>
      <p>
        Take a look at what's going on under the hood to better understand why
      </p>

      <div>Response From API</div>
      <div>{data.value}</div>
    </>
  );
}
