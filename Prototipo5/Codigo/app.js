const API = 'http://localhost:5000/api';
let usuariActual = null;

// ──────────────────────────────────────────
// NAVEGACIÓ
// ──────────────────────────────────────────
function mostrarLogin() {
  document.getElementById('seccio-login').style.display = 'block';
  document.getElementById('seccio-registre').style.display = 'none';
  document.getElementById('seccio-dashboard').style.display = 'none';
}

function mostrarRegistre() {
  document.getElementById('seccio-login').style.display = 'none';
  document.getElementById('seccio-registre').style.display = 'block';
  document.getElementById('seccio-dashboard').style.display = 'none';
}

function mostrarDashboard() {
  document.getElementById('seccio-login').style.display = 'none';
  document.getElementById('seccio-registre').style.display = 'none';
  document.getElementById('seccio-dashboard').style.display = 'block';
  document.getElementById('benvinguda').textContent = `Benvingut/da, ${usuariActual.nom}`;
  carregarPistes();
  carregarReserves();
}

// ──────────────────────────────────────────
// AUTH
// ──────────────────────────────────────────
async function login() {
  const email    = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

  if (!email || !password) {
    document.getElementById('login-error').textContent = 'Omple tots els camps.';
    return;
  }

  const res = await fetch(`${API}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  const data = await res.json();

  if (res.ok) {
    usuariActual = data.usuari;
    mostrarDashboard();
  } else {
    document.getElementById('login-error').textContent = data.error;
  }
}

async function registre() {
  const nom      = document.getElementById('reg-nom').value;
  const email    = document.getElementById('reg-email').value;
  const password = document.getElementById('reg-pass').value;

  if (!nom || !email || !password) {
    document.getElementById('reg-error').textContent = 'Omple tots els camps.';
    return;
  }

  const res = await fetch(`${API}/registre`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nom, email, password })
  });
  const data = await res.json();

  if (res.ok) {
    alert('Registre completat! Ara pots iniciar sessió.');
    mostrarLogin();
  } else {
    document.getElementById('reg-error').textContent = data.error;
  }
}

function logout() {
  usuariActual = null;
  mostrarLogin();
}

// ──────────────────────────────────────────
// PISTES
// ──────────────────────────────────────────
async function carregarPistes() {
  const res    = await fetch(`${API}/pistes`);
  const pistes = await res.json();

  const llista = document.getElementById('llista-pistes');
  const sel    = document.getElementById('sel-pista');
  llista.innerHTML = '';
  sel.innerHTML    = '<option value="">-- Selecciona pista --</option>';

  pistes.forEach(p => {
    llista.innerHTML += `<div class="pista-item">🏅 <strong>${p.nom}</strong> — ${p.tipus} | 📍 ${p.centre}, ${p.ciutat}</div>`;
    sel.innerHTML    += `<option value="${p.id_pista}">${p.nom} (${p.tipus})</option>`;
  });
}

// ──────────────────────────────────────────
// SCHEDULES
// ──────────────────────────────────────────
async function carregarSchedules() {
  const id_pista = document.getElementById('sel-pista').value;
  const selSch   = document.getElementById('sel-schedule');
  selSch.innerHTML = '<option value="">-- Selecciona horari --</option>';

  if (!id_pista) return;

  const res       = await fetch(`${API}/schedules/pista/${id_pista}`);
  const schedules = await res.json();

  schedules.forEach(s => {
    if (s.disponible) {
      selSch.innerHTML += `<option value="${s.id_schedule}">${s.data} | ${s.hora_inici} - ${s.hora_fi}</option>`;
    }
  });

  if (selSch.options.length === 1) {
    selSch.innerHTML = '<option value="">No hi ha horaris disponibles</option>';
  }
}

// ──────────────────────────────────────────
// RESERVES
// ──────────────────────────────────────────
async function crearReserva() {
  const id_schedule = document.getElementById('sel-schedule').value;
  const msg         = document.getElementById('reserva-msg');

  if (!document.getElementById('sel-pista').value) {
    msg.style.color = '#e53935';
    msg.textContent = 'Selecciona una pista.';
    return;
  }
  if (!id_schedule) {
    msg.style.color = '#e53935';
    msg.textContent = 'Selecciona un horari.';
    return;
  }

  const res = await fetch(`${API}/reserves`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id_usuari: usuariActual.id_usuari, id_schedule })
  });
  const result = await res.json();

  if (res.ok) {
    msg.style.color = 'green';
    msg.textContent = result.missatge;
    carregarReserves();
    carregarSchedules();
  } else {
    msg.style.color = '#e53935';
    msg.textContent = result.error;
  }
}

async function carregarReserves() {
  const res      = await fetch(`${API}/reserves/usuari/${usuariActual.id_usuari}`);
  const reserves = await res.json();
  const cos      = document.getElementById('cos-reserves');
  cos.innerHTML  = '';

  if (reserves.length === 0) {
    cos.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#999">No tens reserves</td></tr>';
    return;
  }

  reserves.forEach(r => {
    cos.innerHTML += `
      <tr>
        <td>${r.pista}</td>
        <td>${r.tipus}</td>
        <td>${r.centre} (${r.ciutat})</td>
        <td>${r.data}</td>
        <td>${r.hora_inici} - ${r.hora_fi}</td>
        <td><button class="btn-cancel" onclick="cancellarReserva(${r.id_reserva})">Cancel·lar</button></td>
      </tr>`;
  });
}

async function cancellarReserva(id_reserva) {
  if (!confirm('Segur que vols cancel·lar aquesta reserva?')) return;

  const res = await fetch(`${API}/reserves/${id_reserva}`, { method: 'DELETE' });
  if (res.ok) {
    carregarReserves();
    carregarSchedules();
  }
}
