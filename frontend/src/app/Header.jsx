export default function Header() {
  return (
    <header className="bg-sky shadow-sm px-6 py-3 flex justify-between items-center">
      <nav className="space-x-4">
        <h1 className="text-2xl font-bold">
          <a href="/app" className="text-white hover:text-gray-300">
            Panel de Huéspedes
          </a>
        </h1>
      </nav>
    </header>
  );
}
