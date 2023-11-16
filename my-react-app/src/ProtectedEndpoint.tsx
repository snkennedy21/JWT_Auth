import { useProtectedEndpointQuery } from "./store/mainApi";
import { useEffect } from "react";

export default function ProtectedEndpoint() {
  const { data, isLoading, error, refetch } = useProtectedEndpointQuery();

  useEffect(() => {
    if (error?.data?.detail === "Expired Token") {
      refetch();
    }
  }, [error, refetch]);

  if (isLoading) return <div>Is Loading</div>;

  return (
    <>
      <div className="py-24 sm:py-32">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl lg:text-center">
            <h2 className="text-base font-semibold leading-7 text-indigo-600">
              Protected Page
            </h2>
            <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              This page is fully protected by authentication requirements.
            </p>
            {error ? (
              <p className="mt-6 text-lg leading-8 text-gray-600">
                Uh Oh! It looks like you tried to access an API endpoint
                protected by Authentication Requirements. If you open your
                console, you should see a 401 error. You should be able to see
                the contents of this page by signing into an account
              </p>
            ) : (
              <p className="mt-6 text-lg leading-8 text-gray-600">
                This page is fully protected by authentication requirements. You
                can only access the data from the associated endpoint when you
                are signed in as an authenticated user. Take a look at what's
                going on under the hood to better understand why
              </p>
            )}

            <div>Response From API</div>
            {error ? (
              <>
                <div>{error.status}</div>
                <div>{error.data.detail}</div>
              </>
            ) : (
              <div>{data.user}</div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
