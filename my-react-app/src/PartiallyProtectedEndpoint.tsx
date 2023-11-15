import { usePartiallyProtectedEndpointQuery } from "./store/mainApi";

export default function PartiallyProtectedEndpoint() {
  const { data, isLoading } = usePartiallyProtectedEndpointQuery();

  if (isLoading) return <div>Is Loading</div>;
  return (
    <>
      <div className="py-24 sm:py-32">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl lg:text-center">
            <h2 className="text-base font-semibold leading-7 text-indigo-600">
              Partially Protected Page
            </h2>
            <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              This page is partially protected by authentication requirements.
            </p>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Anyone can access this page and the API endpoint associated with
              it, but you can make decisions on the backend based on the users
              authentication status. Take a look at what's going on under the
              hood to better understand why
            </p>
            <div>Response From API</div>
            <div>{data.user}</div>
          </div>
        </div>
      </div>
    </>
  );
}
