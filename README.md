# Alkimia Backend Core | Fintech Infrastructure

Alkimia Backend Core is the foundation of Castle Trade's financial services ecosystem, engineered for high-availability, precision auditing, and global scalability.

## Institutional Architecture

The platform utilizes a modular microservices architecture designed to manage complex financial flows with ACID-compliant integrity.

### Modular Ecosystem (`src/`)
- **`api/`**: Core endpoints and transaction controllers.
- **`services/`**: Business logic including commission calculation and ledger management.
- **`webhooks/`**: Specialized handlers for high-integrity event ingestion (Stripe).
- **`middleware/`**: Security enforcement, rate limiting, and JWT validation.

### Financial Data Integrity
To maintain institutional-grade records, the platform follows strict protocols:
- **Double-Entry Ledger Architecture**: Every transaction is recorded with immutable audit trails.
- **Idempotency Keys**: Enforced across all API endpoints to prevent duplicate processing.
- **Periodic Reconciliation**: Automated verification against external provider state.

### DevSecOps & Portability
- **Infrastructure as Code**: Optimized `Dockerfile` for standardized deployment across AWS and global cloud regions.
- **Testing Rigor**: Comprehensive unit and integration test suites in `/tests` to ensure financial correctness.
- **API Documentation**: Detailed specification in `/docs` for seamless institutional integration.

## Core Features
- **Secure Webhook Ingestion**: Signature-verified event handling for high-integrity updates.
- **Supabase Identity Wrapper**: Secure JWT-based authentication with MFA enforcement.
- **Distributed Observability**: Integrated logging and monitoring for real-time SRE situational awareness.

---
**Technical Note**: This repository contains the architectural skeleton of the Alkimia Backend. Business-specific alpha logic is abstracted to maintain firm privacy.

(c) 2026 Castle Trade LLC. Proprietary and Confidential.
