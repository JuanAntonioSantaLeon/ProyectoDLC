import { useEffect, useState } from "react";

export default function GuestsList() {
  const [guests, setGuests] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/guests/")
      .then((res) => res.json())
      .then((data) => setGuests(data));
  }, []);

  return (
    <div className="max-w-5xl mx-auto">
      <h2 className="text-2xl font-semibold mb-4 text-gray-800">Huéspedes</h2>

      <div className="bg-white shadow rounded-lg divide-y">
        {guests.map((guest) => (
          <div
            key={guest.id}
            className="flex justify-between items-center p-4 hover:bg-gray-50 cursor-pointer"
            onClick={() => (window.location.href = `/app/guest/${guest.id}`)}
          >
            <div>
              <h3 className="font-medium text-gray-800">
                {guest.first_name} {guest.last_name}
              </h3>
              <p className="text-sm text-gray-500">
                Última estancia:{" "}
                {guest.last_stay
                  ? `${new Date(
                      guest.last_stay.check_in
                    ).toLocaleDateString()} → ${new Date(
                      guest.last_stay.check_out
                    ).toLocaleDateString()}`
                  : "—"}
              </p>
            </div>
            <span className="text-gray-400 text-sm">Ver detalles →</span>
          </div>
        ))}
      </div>
    </div>
  );
}
