# Learnings: PydanticAI Framework

## 1. Structured Output (Schema)

The core philosophy of PydanticAI is that LLM interactions should be treated like data validation. By using Pydantic models, you enforce strict type-safety on LLM responses.

- **Guaranteed Shape:** The LLM is forced to return data that fits a defined BaseModel.

- **Automatic Retries:** If the LLM output fails validation (e.g., a missing field or wrong type), the framework automatically sends the error back to the LLM to "fix" its own mistake.

- **Usage:** Defined via the result_type parameter in the Agent constructor.

---

## 2. Tool Use (Function Calling)

Tools allow the agent to perform actions or fetch real-time data. PydanticAI uses Python's type hints to tell the LLM how to use them.

- **Self-Documenting:** Tool metadata (descriptions, arguments) is inferred directly from the function signature and docstrings.

- **@agent.tool:** Used for tools that require access to the RunContext (e.g., accessing a database or API key defined in the agent's dependencies).

- **@agent.tool_plain:** Used for "pure" functions that only need their input arguments and do not require any external agent state.

- **Lazy Discovery:** Tools can be added to an agent dynamically at runtime.

---

## 3. Agent Context (Dependency Injection)

This pattern keeps agents "stateless" and highly testable by "injecting" external services.

- **Deps Class:** A Python class (usually a Dataclass or BaseModel) containing services, API clients, or database connections.

- **RunContext:** Within a tool, you access these dependencies via ctx.deps.

- **Security:** Sensitive credentials stay in your control and aren't leaked into the LLM prompt unless explicitly defined in the logic.

---

## 4. Testing & Evals**

Because PydanticAI is built on standard Python patterns, testing is significantly more robust than in "prompt-only" frameworks.

### Unit Testing Tools

- **Isolated Testing:** Since tools are standard functions, they can be tested individually.

- **Mocking Context:** You can manually create a RunContext object to test tool behavior with specific mocked dependencies (like a mock database).

### Integration & Monitoring

- **capture_run_messages:** A context manager that records every message sent to and from the LLM. This allows you to assert that the agent actually called the correct tool in a specific sequence.

- **Test Node:** Run agents in "Test Mode" to bypass LLM costs and use recorded/mocked responses for CI/CD pipelines.

### Systematic Evaluations (Evals)

- **Golden Test Sets:** Creating a suite of prompt/response pairs to ensure the agent's logic remains consistent over time.

- **Performance Benchmarking:** Quantifying how often the agent chooses the correct tool versus attempting a direct answer.
