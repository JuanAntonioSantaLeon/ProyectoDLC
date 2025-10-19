export default function Testimonials() {
  return (
    <section className="py-20 bg-mint text-center">
      <h3 className="text-3xl font-bold mb-10">What Our Guests Say</h3>
      <div className="max-w-4xl mx-auto space-y-8">
        <blockquote className="bg-white p-8 rounded-xl shadow">
          <p className="text-lg italic">“Absolutely wonderful stay. The staff was incredible!”</p>
          <footer className="mt-4 font-semibold text-crimson">— Maria L.</footer>
        </blockquote>
      </div>
    </section>
  );
}
