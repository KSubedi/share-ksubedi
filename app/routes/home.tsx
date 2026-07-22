import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Share" },
    { name: "description", content: "Personal sharing site by Kaushal Subedi" },
  ];
}

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gray-50 p-4">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900">Share</h1>
        <p className="mt-2 text-sm text-gray-600">
          Personal sharing site by Kaushal Subedi.
        </p>
      </div>
    </main>
  );
}