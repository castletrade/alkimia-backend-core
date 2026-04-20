# Alkimia API Specification v1.0
## Castle Trade LLC | Institutional Fintech Documentation

This document specifies the internal and external endpoints for the Alkimia Backend infrastructure.

### 1. Authentication
All requests must be authenticated via the `Authorization: Bearer <JWT>` header. Tokens are issued via Supabase Auth.

### 2. Webhooks
Endpoints designed for event-driven interaction with third-party providers.

#### `POST /webhooks/stripe`
Handles incoming events from Stripe Connect.
- **Headers**: `Stripe-Signature` (Required)
- **Security**: Signature verification via HMAC-SHA256.
- **Events Supported**: `account.updated`, `transfer.created`, `payout.failed`.

### 3. Financial Services
Core API for platform financial operations.

#### `GET /api/v1/ledger/balance`
Retrieves the real-time balance of an institutional account.
- **Parameters**: `account_id` (Query String)
- **Response**: 
```json
{
  "account_id": "string",
  "balance": "decimal",
  "currency": "ISO_CODE"
}
```

#### `POST /api/v1/transfer`
Initiates an internal ledger transfer between platform accounts.
- **Body**: `destination_account`, `amount`, `idempotency_key`.
- **Response**: `201 Created` on success.

---
**Confidentiality Note**: This specification is proprietary to Castle Trade LLC.
