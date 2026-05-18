const inp1 = document.getElementById('inp1');
const inp2 = document.getElementById('inp2');

function setValid(input, iconId) {
    input.classList.remove('invalid');
    input.classList.add('valid');
    const icon = document.getElementById(iconId);
    icon.textContent = '✔';
    icon.style.color = '#28a745';
    icon.style.display = 'block';
}

function setInvalid(input, iconId) {
    input.classList.remove('valid');
    input.classList.add('invalid');
    const icon = document.getElementById(iconId);
    icon.textContent = '✖';
    icon.style.color = '#dc3545';
    icon.style.display = 'block';
}

function showError(id, msg) {
    document.getElementById(id).textContent = msg;
}

function clearError(id) {
    document.getElementById(id).textContent = '';
}

/* ── Username ── */
function validateUsername() {
    const val = inp1.value.trim();
    if (val === '') {
        setInvalid(inp1, 'icon-username');
        showError('err-username', 'Username is required.');
        return false;
    }
    if (val.length < 3) {
        setInvalid(inp1, 'icon-username');
        showError('err-username', 'Username must be at least 3 characters.');
        return false;
    }
    if (!/^[a-zA-Z0-9_]+$/.test(val)) {
        setInvalid(inp1, 'icon-username');
        showError('err-username', 'Only letters, numbers, and underscores allowed.');
        return false;
    }
    setValid(inp1, 'icon-username');
    clearError('err-username');
    return true;
}

/* ── Password ── */
function validatePassword() {
    const val = inp2.value;
    if (val === '') {
        setInvalid(inp2, 'icon-password');
        showError('err-password', 'Password is required.');
        return false;
    }
    if (val.length < 8) {
        setInvalid(inp2, 'icon-password');
        showError('err-password', 'Password must be at least 8 characters.');
        return false;
    }
    setValid(inp2, 'icon-password');
    clearError('err-password');
    return true;
}

/* ── Live listeners ── */
inp1.addEventListener('input', validateUsername);
inp1.addEventListener('blur',  validateUsername);

inp2.addEventListener('input', validatePassword);
inp2.addEventListener('blur',  validatePassword);

/* ── Submit ── */
document.getElementById('loginForm').addEventListener('submit', function (e) {
    const u = validateUsername();
    const p = validatePassword();
    if (!u || !p) {
        e.preventDefault();
        const firstInvalid = document.querySelector('input.invalid');
        if (firstInvalid) firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
});