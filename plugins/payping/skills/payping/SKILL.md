---
name: payping
description: "PayPing merchant account for agents: balance, sales, invoices; create invoices and payment links. Use when the user asks about PayPing (payping.ir) or wants to manage their own PayPing merchant account in Iran."
---

# PayPing

PayPing merchant account for agents: balance, sales, invoices; create invoices and payment links.

The tools below come from the `payping-mcp` MCP server. If they are not available, install it with `claude mcp add payping -- uvx payping-mcp`, or add `"payping": {"command": "uvx", "args": ["payping-mcp"], "env": {"PAYPING_TOKEN": "${PAYPING_TOKEN:-}"}}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `payping_get_profile`: Show the PayPing account behind PAYPING_TOKEN: username, name, email, phone and verification flags.
- `payping_get_balance`: Current PayPing wallet balance in Toman (money received and not yet withdrawn).
- `payping_get_sales_summary`: Sales totals for a period (default last 30 days): amount in Toman, count, daily averages.
- `payping_list_transactions`: List payments, newest first, with total count.
- `payping_get_payment`: One payment by code: amount, payer, fees, refund state, paymentStatus and status_text.
- `payping_list_withdrawals`: List settlements (withdrawals to your bank) with total count.
- `payping_get_withdrawal`: One settlement by code: amount, dates, IBAN, bank tracking number.
- `payping_list_customers`: List saved customers with total count.
- `payping_get_customer`: One customer by code.
- `payping_list_products`: List products (PayPing "financial items") with total count.
- `payping_get_product`: One product by code.
- `payping_list_coupons`: List discount coupons (type 0 = percent, 1 = Toman) with total count.
- `payping_get_coupon`: One coupon by code: expiry, max uses, buyers and their spend.
- `payping_list_invoices`: List invoices (status 0 draft, 1 awaiting payment, 2 paid, 3 overdue, 4 cancelled) with total count.
- `payping_get_invoice`: One invoice by code with items, customer, status and `url` (public pay page).
- `payping_create_customer`: Save a new customer; returns its `code` (needed for invoices).
- `payping_create_product`: Create a product; returns its `code`.
- `payping_create_payment_link`: Make a permanent public payment page for a product; returns `url`.
- `payping_create_coupon`: Create an active discount coupon; returns its `code`.
- `payping_create_invoice`: Create an invoice for a saved customer; returns `code`, `payCode`, `url` (pay page).
- `payping_send_invoice`: Send an invoice to its customer by SMS/email.

## Rules

- This server acts on the user's own account (`PAYPING_TOKEN`). Confirm with the user before any call that creates, sends, edits or deletes something.
- On timeouts or HTTP 403 outside Iran, set `PAYPING_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
