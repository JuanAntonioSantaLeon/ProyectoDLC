import heroImage from "../assets/hero.jpg";

export default function Hero() {
  return (
    <section
      className="relative h-[80vh] flex items-center justify-center text-center bg-cover bg-center"
      style={{ backgroundImage: `url(${heroImage})` }}
    >
      <div className="absolute inset-0 bg-[#5D5F71]/70"></div> {/* overlay */}
      <div className="relative z-10 max-w-3xl text-white px-6">
        <h2 className="text-5xl font-bold mb-4">Luxury Awaits You</h2>
        <p className="text-lg mb-6">
          Experience comfort, elegance, and serenity in every stay.
        </p>
        <button className="bg-[#FE938C] hover:bg-[#B80C09] px-6 py-3 rounded-full font-semibold transition">
          Explore Rooms
        </button>
      </div>
    </section>
  );
}
