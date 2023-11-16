import { Link } from "react-router-dom";

export default function HeroSection() {
  return (
    <div className="mx-auto max-w-2xl py-44">
      <div className="hidden sm:mb-8 sm:flex sm:justify-center">
        <div className="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
          Check out the{" "}
          <a
            href="https://github.com/snkennedy21/JWT_Auth#readme"
            className="font-semibold text-indigo-600"
            target="_blank"
          >
            <span className="absolute inset-0" aria-hidden="true" />
            Documentation <span aria-hidden="true">&rarr;</span>
          </a>
        </div>
      </div>
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
          Build Your Next Project Faster
        </h1>
        <p className="mt-6 text-lg leading-8 text-gray-600">
          Your one stop solution for creating applications with modern
          technologies
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <Link
            to="/signup"
            className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Get started
          </Link>
          <a
            href="https://github.com/snkennedy21/JWT_Auth#readme"
            className="text-sm font-semibold leading-6 text-gray-900"
            target="_blank"
          >
            Learn more <span aria-hidden="true">→</span>
          </a>
        </div>
      </div>
    </div>
  );
}
