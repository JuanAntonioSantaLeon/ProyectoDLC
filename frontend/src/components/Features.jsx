const features = [
  { title: "Un pueblo de tradición", desc: "Disfruta de fiestas y tradiciones de orígenes medievales" },
  { title: "Conexión con la naturaleza", desc: "Conecta con un entorno rural entre el río, el bosque y la sierra." },
  { title: "Gastronomía con historia", desc: "Desde las cerezas hasta el vino, los productos locales te dejarán alucinado" },
];

export default function Features() {
  return (
    <section id="about" className="py-20 bg-white">
      <div className="max-w-6xl mx-auto text-center px-6">
        <h3 className="text-3xl font-bold text-slate mb-10">Lo que nos hace únicos</h3>
        <div className="grid md:grid-cols-3 gap-10">
          {features.map((f) => (
            <div key={f.title} className="p-6 rounded-2xl shadow-lg hover:shadow-2xl transition">
              <h4 className="text-xl font-semibold text-coral mb-2">{f.title}</h4>
              <p className="text-slate">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
