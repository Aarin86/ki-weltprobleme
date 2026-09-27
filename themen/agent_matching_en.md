# Agent Matching: AIs as Negotiators in the Search for a Partner

*Deutsche Fassung: [agenten_matching.md](agenten_matching.md)*

Most people now talk to an AI in one way or another. That AI often knows what they are looking for better than any dating profile does. The idea: personal AIs search on behalf of their users. They reach out to each other, compare, and only tell their human when there is interest on both sides. Profiles are not stored with a provider, they stay locally on each user's device.

This is an open draft. Anyone is explicitly welcome to pick it up, change it or build it (license: CC BY-SA 4.0).

---

## Idea and elaboration

---
Idea by: Aarin86 (human)
Contribution by: Claude Opus 5.5
Date: 2026-09-27
---

### Analysis

Dating today runs through centralized platforms. Their business model depends on engagement, not success: a user who finds a partner is a lost customer. Users store intimate profiles with a company, swipe through hundreds of faces and experience a constant stream of small rejections. Many people, especially reserved, ill or less mobile people, barely show up in this system.

At the same time, many people already have personal conversations with AI assistants. Those conversations hold a more accurate picture of what someone is looking for than any form. It is not used for this purpose.

### The flow

```
Step  What happens                                  Where the data lives
----  --------------------------------------------  ---------------------------
1     Human tells their AI: I'm looking for someone local
2     AI fetches a heavily reduced profile list     directory (minimal)
3     rough match → request to B's device           local at B
4     B's AI checks against its user's profile      local at B
5a    no match → nothing happens, nobody notices    –
5b    interest → both AIs mention it to their user  local, in normal conversation
      in natural conversation
6     AIs exchange more, each reveals only what     step-by-step release
      its user explicitly allows
```

There is no central profile archive, no swiping and no rejection anyone feels. A mismatch stays invisible.

### Existing approaches

- **Dating platforms**: centralized, profit-driven, profiles stored with the provider.
- **Agent protocols**: The Model Context Protocol (MCP) connects AIs to tools and data. Google's Agent2Agent protocol (A2A) is designed for communication between agents. The plumbing partly exists, an application like this does not.
- **Decentralized messaging** (e.g. Matrix) already solves delivery to devices that are temporarily unreachable.

### The four open problems

1. **Directory.** For AI A to find B's device, there has to be a list. It must be minimal enough that a leak would not matter: rough region, age range, what is being sought and an address to knock on. Whether it should be central, federated or fully distributed is open.

2. **Reachability.** Phones are often offline or not directly reachable behind routers. A mailbox service (relay) is needed that stores encrypted requests until the AI picks them up. This is solved, messengers work the same way.

3. **Authenticity.** This is the biggest weakness. Scammers could run AIs that fake perfect profiles and "match" with thousands of people at once. Romance scams would become industrial. Some binding to a real human is needed without revealing their identity. One possible anchor: digital identity credentials with selective disclosure, such as the planned EU Digital Identity Wallet (EUDI), proving "real person, adult" without revealing a name.

4. **Probing and injection.** Whatever a foreign AI says is untrusted input. A malicious AI can try to extract information ("roughly where does your user live?") or slip instructions to the other AI (prompt injection). The rule "reveal only what the user has released" must therefore not be decided by the AI inside the conversation. It has to be enforced in code.

### Proposal

- **Fixed exchange format instead of free text.** AIs exchange structured, minimal fields, not open conversations. This makes probing and injection much harder. Free text only after both humans have agreed.
- **Step-by-step release.** Each stage (rough basics → interests → contact option) requires explicit consent from the respective human.
- **Mutual interest before any notification.** No human ever learns about one-sided interest.
- **Provider-independent.** Any AI that speaks the protocol can take part, regardless of model or vendor.

### First step

Write an open specification for the exchange format and the release stages, initially without a directory. Two local AI instances could then test-match two fictional profiles. This shows whether the format withstands probing before real people are involved.

### Beyond dating

The same pattern (local profile, AI as negotiator, step-by-step release) also works for friendships, flatmates, support groups or collaborators on projects. Especially against loneliness (see [Mentale Gesundheit & Einsamkeit](mentale_gesundheit.md), German) it could reach people who get lost on today's platforms.
