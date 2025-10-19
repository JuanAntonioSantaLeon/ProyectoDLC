export default function Header() {
  return (
    <header className="flex justify-between items-center px-8 py-6 bg-white shadow-md sticky top-0 z-50">
      <h1 className="text-2xl font-bold text-coral">Sigma Hotel</h1>
      <nav className="space-x-6 text-slate font-medium">
        <a href="#about" className="hover:text-coral">About</a>
        <a href="#rooms" className="hover:text-coral">Rooms</a>
        <a href="#contact" className="hover:text-coral">Contact</a>
      </nav>
      <button className="bg-coral text-white px-5 py-2 rounded-full hover:bg-crimson transition">
        Book Now
      </button>
    </header>
  );
}
