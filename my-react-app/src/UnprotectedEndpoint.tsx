import { useUnprotectedEndpointQuery } from "./store/mainAPI";

export default function UnprotectedEndpoint() {
  const { data, isLoading } = useUnprotectedEndpointQuery();

  if (isLoading) return <div>Is Loading</div>;

  return (
    <>
      <div>Hello</div>
      <div className="py-24 sm:py-32">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl lg:text-center">
            <h2 className="text-base font-semibold leading-7 text-indigo-600">
              Unprotected Page
            </h2>
            <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              This page is not protected by authentication requirements.
            </p>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Anyone can access this page and the API endpoint associated with
              it. Take a look at what's going on under the hood to better
              understand why
            </p>
            <div>Response From API</div>
            <div>{data.value}</div>
          </div>
        </div>
      </div>
    </>
  );
}
