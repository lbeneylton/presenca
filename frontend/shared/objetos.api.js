// Objeto para POST
export const POST = (payload) => ({
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
});


// Objeto para PUT
export const PUT = (payload) => ({
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
});


