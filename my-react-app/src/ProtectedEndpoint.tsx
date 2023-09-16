import { useProtectedEndpointQuery } from "./store/mainAPI";

export default function ProtectedEndpoint() {
  const { data, isLoading, error } = useProtectedEndpointQuery();

  console.log(data);

  if (isLoading) return <div>Is Loading</div>;

  if (error)
    return (
      <div>
        Uh Oh! It looks like you tried to access an API endpoint protected by
        Authentication. If you open your console, you should see a 401 error.
        You should be able to see the contents of this page by signing into an
        account
      </div>
    );

  return (
    <>
      <div>
        This page is fully protected by authentication requirements. You can
        only access the data from the associated endpoint when you are signed in
        as an authenticated user.
      </div>
      <p>
        Take a look at what's going on under the hood to better understand why
      </p>

      <div>Response From API</div>
      <div>{data.user}</div>
    </>
  );
}
