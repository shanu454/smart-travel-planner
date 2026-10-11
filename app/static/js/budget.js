/**
 * Budget Module: Spending analysis, donut charts, and live currency converter.
 */

const CATEGORY_COLORS = {
  "Food & Dining": "#f59e0b",     // Amber
  "Accommodation": "#6366f1",     // Indigo
  "Transport": "#06b6d4",         // Cyan
  "Activities": "#8b5cf6",        // Violet
  "Shopping": "#ec4899",          // Pink
  "Other": "#64748b"              // Slate
};

let cachedRates = {};

function renderBudgetSummary(budgetSummary, currency = "USD", daysCount = 1) {
  if (!budgetSummary) return;

  const totalEl = document.getElementById("budget-stat-total");
  const spentEl = document.getElementById("budget-stat-spent");
  const remainEl = document.getElementById("budget-stat-remaining");
  const spentPctEl = document.getElementById("budget-spent-percent");
  const progBar = document.getElementById("budget-progress-bar");
  const progLabel = document.getElementById("budget-progress-label");
  const dailyEl = document.getElementById("budget-daily-allowance");
  const currCodeEl = document.getElementById("budget-curr-code");

  const sym = getCurrencySymbol(currency);

  if (totalEl) totalEl.textContent = `${sym}${budgetSummary.total_budget.toLocaleString('en-US', { minimumFractionDigits: 2 })}`;
  if (spentEl) spentEl.textContent = `${sym}${budgetSummary.total_spent.toLocaleString('en-US', { minimumFractionDigits: 2 })}`;
  if (remainEl) remainEl.textContent = `${sym}${budgetSummary.remaining_budget.toLocaleString('en-US', { minimumFractionDigits: 2 })}`;
  if (spentPctEl) spentPctEl.textContent = `${budgetSummary.percent_used}% of budget`;
  if (currCodeEl) currCodeEl.textContent = currency;

  if (progBar) progBar.style.width = `${Math.min(100, budgetSummary.percent_used)}%`;
  if (progLabel) progLabel.textContent = `${budgetSummary.percent_used}%`;

  // Safe daily allowance
  const safeDaily = daysCount > 0 ? (budgetSummary.remaining_budget / daysCount) : 0;
  if (dailyEl) dailyEl.textContent = `${sym}${safeDaily.toFixed(0)} / day`;

  // Draw Category Donut Chart
  drawDonutChart("budget-canvas", budgetSummary.by_category, sym);
  renderCategoryLegend("category-legend-list", budgetSummary.by_category, budgetSummary.total_spent, sym);
}

function renderExpenseTable(expenses, currency, onDeleteExpense) {
  const tbody = document.getElementById("expense-table-body");
  if (!tbody) return;

  tbody.innerHTML = "";
  const sym = getCurrencySymbol(currency);

  if (!expenses || expenses.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color: var(--text-dim); padding: 1.5rem;">No expenses logged yet. Click "+ Log Expense" above.</td></tr>`;
    return;
  }

  expenses.forEach(exp => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><strong>${escapeHtml(exp.title)}</strong></td>
      <td><span class="category-tag" style="border-left: 3px solid ${CATEGORY_COLORS[exp.category] || '#ccc'}">${escapeHtml(exp.category)}</span></td>
      <td>${escapeHtml(exp.date)}</td>
      <td style="font-weight: 700; color: var(--text-main);">${sym}${exp.amount.toFixed(2)}</td>
      <td>
        <button class="btn-icon-delete" data-id="${exp.id}" title="Delete Expense">🗑️</button>
      </td>
    `;

    const delBtn = tr.querySelector(".btn-icon-delete");
    if (delBtn) {
      delBtn.addEventListener("click", () => onDeleteExpense(exp.id));
    }
    tbody.appendChild(tr);
  });
}

function drawDonutChart(canvasId, byCategory, sym) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  const total = Object.values(byCategory).reduce((acc, v) => acc + v, 0);

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const radius = Math.min(centerX, centerY) - 20;
  const innerRadius = radius * 0.65;

  if (total <= 0) {
    // Empty state ring
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.arc(centerX, centerY, innerRadius, 2 * Math.PI, 0, true);
    ctx.fillStyle = "rgba(255, 255, 255, 0.06)";
    ctx.fill();

    ctx.fillStyle = "#64748b";
    ctx.font = "600 13px 'Plus Jakarta Sans'";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("No Expenses", centerX, centerY);
    return;
  }

  let startAngle = -Math.PI / 2;

  Object.entries(byCategory).forEach(([cat, amt]) => {
    if (amt <= 0) return;
    const sliceAngle = (amt / total) * 2 * Math.PI;

    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, startAngle, startAngle + sliceAngle);
    ctx.arc(centerX, centerY, innerRadius, startAngle + sliceAngle, startAngle, true);
    ctx.closePath();

    ctx.fillStyle = CATEGORY_COLORS[cat] || "#94a3b8";
    ctx.fill();

    startAngle += sliceAngle;
  });

  // Center text
  ctx.fillStyle = "#ffffff";
  ctx.font = "700 16px 'Outfit'";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(`${sym}${total.toFixed(0)}`, centerX, centerY - 8);

  ctx.fillStyle = "#94a3b8";
  ctx.font = "500 11px 'Plus Jakarta Sans'";
  ctx.fillText("Total Spent", centerX, centerY + 12);
}

function renderCategoryLegend(legendId, byCategory, totalSpent, sym) {
  const container = document.getElementById(legendId);
  if (!container) return;

  container.innerHTML = "";

  Object.entries(byCategory).forEach(([cat, amt]) => {
    const pct = totalSpent > 0 ? ((amt / totalSpent) * 100).toFixed(0) : 0;
    const row = document.createElement("div");
    row.className = "legend-row";
    row.innerHTML = `
      <div class="legend-label-wrap">
        <div class="legend-color-box" style="background: ${CATEGORY_COLORS[cat] || '#ccc'}"></div>
        <span>${escapeHtml(cat)}</span>
      </div>
      <div>
        <strong>${sym}${amt.toFixed(2)}</strong>
        <span style="color: var(--text-dim); font-size: 0.75rem; margin-left: 0.35rem;">(${pct}%)</span>
      </div>
    `;
    container.appendChild(row);
  });
}

async function initCurrencyConverter(defaultFrom = "INR", defaultTo = "USD") {
  const fromSel = document.getElementById("convert-from-curr");
  const toSel = document.getElementById("convert-to-curr");
  const amtInput = document.getElementById("convert-input-amt");
  const resultEl = document.getElementById("converter-result");

  if (!fromSel || !toSel || !amtInput || !resultEl) return;

  const popular = ["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CAD", "SGD", "CHF", "CNY", "THB", "AED"];

  fromSel.innerHTML = popular.map(c => `<option value="${c}" ${c === defaultFrom ? 'selected' : ''}>${c}</option>`).join("");
  toSel.innerHTML = popular.map(c => `<option value="${c}" ${c === defaultTo ? 'selected' : ''}>${c}</option>`).join("");

  async function updateConversion() {
    const from = fromSel.value;
    const to = toSel.value;
    const amt = parseFloat(amtInput.value) || 0;

    if (!cachedRates[from]) {
      try {
        const res = await fetch(`/api/currency/rates?base=${from}`);
        if (res.ok) {
          const data = await res.json();
          cachedRates[from] = data.rates;
        }
      } catch (e) {
        console.error("Rates fetch error:", e);
      }
    }

    const rates = cachedRates[from] || {};
    const rate = rates[to] || 1.0;
    const converted = (amt * rate).toFixed(2);
    const toSym = getCurrencySymbol(to);
    resultEl.textContent = `= ${toSym}${converted} ${to}`;
  }

  fromSel.addEventListener("change", updateConversion);
  toSel.addEventListener("change", updateConversion);
  amtInput.addEventListener("input", updateConversion);

  updateConversion();
}

function getCurrencySymbol(curr) {
  const map = {
    USD: "$",
    EUR: "€",
    GBP: "£",
    JPY: "¥",
    INR: "₹",
    AUD: "A$",
    CAD: "C$",
    CHF: "Fr",
    CNY: "¥"
  };
  return map[curr] || `${curr} `;
}

function escapeHtml(str) {
  return String(str || "").replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
}

window.BudgetModule = {
  renderBudgetSummary,
  renderExpenseTable,
  initCurrencyConverter,
  getCurrencySymbol
};
