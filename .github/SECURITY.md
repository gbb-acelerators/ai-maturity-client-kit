# Security policy

## Reporting a vulnerability

Do not report security vulnerabilities through public GitHub issues.

Report them to the Microsoft Security Response Center (MSRC) at
[https://msrc.microsoft.com/create-report](https://msrc.microsoft.com/create-report),
or by email to [secure@microsoft.com](mailto:secure@microsoft.com). See
[Microsoft's security policy](https://www.microsoft.com/msrc/cvd) for the
coordinated disclosure process.

Include as much of the following as you can:

- the type of issue (for example, script injection or data exposure);
- the paths of the affected files;
- the steps to reproduce the issue;
- the impact, including how an attacker could exploit it.

## Client data

The kit runs locally and does not send assessment data to any service.
Client inputs (`responses.json`, Forms exports, survey exports, Copilot
metrics, DORA metrics and everything under `output/`) are ignored by git.

- Never attach client data to an issue, a pull request or a discussion.
- To show a problem, use the mock data (`make demo`,
  `responses.v2.json.example`, the survey `mock-responses-*.json` files) or
  a redacted copy.
- The Learning Survey is identified (name and email). Treat its exports
  and the training plan as personal data.
