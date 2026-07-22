import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Share" },
    { name: "description", content: "Share files easily with share.ksubedi.com" },
  ];
}

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gray-50 p-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-900">Share</h1>
          <p className="mt-2 text-sm text-gray-600">
            Share files easily and securely.
          </p>
        </div>

        <div className="flex flex-col gap-4">
          <label
            htmlFor="file-upload"
            className="flex cursor-pointer items-center justify-center gap-2 rounded-lg border-2 border-dashed border-gray-300 bg-white px-6 py-8 text-center transition-colors hover:border-gray-400"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="text-gray-500"
            >
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            <span className="text-sm text-gray-700">
              Click to upload or drag and drop
            </span>
            <input id="file-upload" type="file" className="hidden" />
          </label>
        </div>
      </div>
    </main>
  );
}