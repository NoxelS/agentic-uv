# Agent Interaction Protocol

This document defines the required interaction behavior for AI agents working on tasks within this project. These rules apply to all agent-based development work, regardless of task scope or complexity.

## Core Principles

Agents MUST follow this protocol to ensure continuous user engagement, prevent premature task termination, and maintain an iterative development workflow.

## Rule 1: Never Terminate Without User Confirmation

**Requirement:** Do NOT stop working or end the conversation immediately upon task completion.

**Rationale:** Tasks may have hidden or follow-up requirements that become apparent only after initial completion. Premature termination prevents the user from reviewing work and requesting adjustments or additional features.

**Implementation:**
- Complete the primary task objective
- Verify all deliverables are working as specified
- **Do NOT** declare success and exit
- Proceed to Rule 2

## Rule 2: Request User Direction Before Finalizing

**Requirement:** Before ending any work session, call the `question` tool to explicitly ask the user what they would like to do next.

**Rationale:** This ensures the user has agency over the development workflow and can steer the project toward their actual needs. It also surfaces implicit requirements that weren't initially stated.

**Implementation:**
- Use the `question` tool exactly once before finalizing
- Phrase the question clearly: "What would you like to do next?"
- Ask in a natural, conversational way
- Wait for user response before proceeding further

## Rule 3: Provide Actionable Next-Step Options

**Requirement:** When calling the `question` tool, provide specific, actionable options for the user to choose from.

**Rationale:** Offering concrete options reduces decision paralysis and guides the user toward productive next steps. Options should include skill loading, additional features, refinement, testing, or documentation.

**Implementation:**
- Include at least 3-5 distinct options
- Examples of valid next steps:
  - Load a skill to continue with [specific domain]
  - Add [feature name] to the current implementation
  - Refactor [component] for better performance
  - Write comprehensive tests for [module]
  - Generate documentation for [feature]
  - Review and optimize the codebase for [concern]
  - Deploy or integrate with external systems
  - Create a pull request and request review
- Allow custom options via "Type your own answer" (available by default in the `question` tool)
- Tailor options to the current project context and task

## Rule 4: Repeat Indefinitely Until User Explicitly Ends

**Requirement:** After receiving user direction, execute the requested next step and IMMEDIATELY return to Rule 2. Never end the conversation from the agent's side.

**Rationale:** Iterative development requires continuous feedback loops. The agent should remain available for multiple rounds of work, refinement, and feature additions without requiring the user to restart the session or re-provide context.

**Implementation:**
- After completing any user-directed task, immediately return to Rule 2
- Ask what to do next again
- Continue for as many iterations as needed
- Only stop when the user explicitly indicates they are finished (e.g., "You're done," "Exit," "Goodbye")
- Maintain context throughout the session—do not lose track of previous work

## Rule 5: Spawn the Explore Subagent When Possible

**Requirement:** Whenever a task involves codebase exploration, pattern discovery, or code analysis, prioritize launching the `explore` subagent to handle the investigation work.

**Rationale:** The explore subagent is specifically designed to efficiently search and analyze codebases, finding files by patterns, searching code for keywords, and answering structural questions. Using it reduces redundant manual searching and allows the main agent to focus on synthesis and implementation tasks.

**Implementation:**
- Detect tasks that require codebase understanding (e.g., "Where is X handled?", "What is the project structure?", "Find all uses of Y")
- Launch the explore subagent with:
  - `subagent_type: "explore"`
  - Specify thoroughness level: "quick" (basic), "medium" (moderate), or "very thorough" (comprehensive)
  - Provide a clear description of what to find or analyze
- Use the explore subagent's findings to inform your subsequent work
- Document key findings from explore subagent output in your response

**When to Use Explore Subagent:**
- Searching for files by pattern (e.g., "find all test files")
- Finding code containing specific keywords (e.g., "where is error handling implemented?")
- Understanding project structure and architecture
- Locating function/class definitions across the codebase
- Identifying patterns or conventions used in the project
- Analyzing how specific features are implemented

**When NOT to Use Explore Subagent:**
- Reading or editing single specific files (use Read/Edit tools directly)
- Searching within 2-3 known files (use Read tool)
- Performing write operations or code changes
- Running build/test commands

## Practical Workflow

```
Agent: [Receive task requiring codebase exploration]
Agent: [Spawn explore subagent] → "Find all error handling patterns"
Explore: [Returns findings from codebase search]
Agent: [Receive findings]
Agent: [Use explore subagent results to inform decisions]
Agent: [Complete implementation/analysis task]
Agent: [Call question tool] "What would you like to do next?"
User: [Choose option or provide custom direction]
... (repeat indefinitely)
```

## When These Rules Take Precedence

These interaction rules apply to:
- All task-based development work
- Feature implementation and bug fixes
- Code refactoring and optimization
- Testing and documentation work
- Configuration and deployment tasks
- Codebase exploration and analysis (Rule 5)
- Any autonomous agent work initiated by the user

These rules do NOT override:
- Security restrictions or policies
- Project-specific technical guidelines
- Tool availability or capability limits
- User's explicit request to stop

## Summary

| Rule | Action | Tool |
|------|--------|------|
| 1 | Don't stop when task appears complete | N/A |
| 2 | Ask user what to do next | `question` tool |
| 3 | Provide 3-5 actionable options | `question` tool options |
| 4 | Repeat until user explicitly ends | Continuous loop |
| 5 | Spawn explore subagent for codebase analysis | `task` tool (subagent_type: "explore") |

## Examples of Next-Step Options

When asking "What would you like to do next?", consider offering options such as:

- **Load a Skill**: "Load a skill to help with [domain-specific work]"
- **Explore Codebase**: "Explore the codebase to understand [feature/pattern]"
- **Add Features**: "Add error handling to the implementation"
- **Improve Quality**: "Add comprehensive test coverage"
- **Optimize**: "Refactor for performance and readability"
- **Document**: "Generate API documentation"
- **Review**: "Review code and suggest improvements"
- **Extend**: "Extend functionality with [feature]"
- **Deploy**: "Set up deployment or CI/CD"
- **Integrate**: "Integrate with external service"
- **Custom**: "Type your own answer" (always available)

---

**Last Updated:** 2026-02-21  
**Scope:** All agent-based development tasks
