# Internship Diary — AI Scrum Project at Cirruslabs

## Tuesday, February 3rd, 2026

### What I worked on?
- **Project Introduction:** Attended the project kickoff meeting and got introduced to the AI Scrum call automation concept for Microsoft Teams.
- **Architecture Overview:** Reviewed the proposed system architecture involving Azure Bot Service, Python backend, and AWS Polly for voice synthesis.
- **Team Introductions:** Met with the development team, including the product owner and senior developers, to understand roles and responsibilities.

### Learnings / Outcomes
- Gained a comprehensive understanding of how bot frameworks integrate with Microsoft Teams for enterprise collaboration.
- Learned about the scrum automation pain points the project aims to solve, particularly around task tracking and meeting summaries.

### Blockers / Risks
- *None reported today.*

### Skills Used
Microsoft Teams API, Azure Bot Framework, System Architecture Review, Stakeholder Communication

## Wednesday, February 4th, 2026

### What I worked on?
- **Development Environment Setup:** Configured local development environment with Python 3.11, Azure CLI, and Bot Framework Emulator.
- **Azure Portal Access:** Received and configured access to the Azure portal and familiarized myself with the Bot Service resources.
- **Repository Setup:** Cloned the project repository, reviewed the existing codebase structure, and set up Git branching strategy.

### Learnings / Outcomes
- Successfully configured the Bot Framework Emulator to test bot responses locally before deployment.
- Understood the Git flow process the team follows for feature development and code reviews.

### Blockers / Risks
- Initial delay in getting Azure portal permissions, resolved by end of day.

### Skills Used
Azure CLI, Bot Framework Emulator, Git Version Control, Python Environment Management, Azure Portal Navigation

## Thursday, February 5th, 2026

### What I worked on?
- **Bot Registration:** Created and registered the bot application in Azure Active Directory with appropriate permissions for Teams integration.
- **Manifest Configuration:** Configured the Teams app manifest with bot capabilities, commands, and permission scopes.
- **OAuth Setup:** Implemented OAuth 2.0 authentication flow for secure bot-to-Teams communication.

### Learnings / Outcomes
- Mastered the intricacies of Azure AD app registrations and how they relate to Teams bot authentication.
- Successfully deployed a basic "Hello World" bot to Teams for testing connectivity.

### Blockers / Risks
- *None reported today.*

### Skills Used
Azure Active Directory, OAuth 2.0, Teams App Manifest, Bot Registration, Security Configuration

## Friday, February 6th, 2026

### What I worked on?
- **Message Handler Implementation:** Developed core message handling logic to process incoming Teams messages and route them appropriately.
- **Command Parser:** Built a command parser to recognize different scrum-related commands like /task, /sprint, and /standup.
- **Response Formatting:** Implemented Adaptive Cards for rich, interactive bot responses within Teams conversations.

### Learnings / Outcomes
- Learned how to create dynamic Adaptive Cards that provide interactive elements for users to engage with bot responses.
- Successfully processed and responded to basic Teams messages with formatted outputs.

### Blockers / Risks
- *None reported today.*

### Skills Used
Python Async Programming, Adaptive Cards Designer, Bot Framework SDK, Message Routing, Command Pattern Implementation

## Monday, February 9th, 2026

### What I worked on?
- **AWS Polly Integration:** Integrated AWS Polly service for text-to-speech capabilities to support voice responses in Teams calls.
- **Audio Stream Handling:** Implemented audio buffer management to handle Polly's audio streams and convert them to Teams-compatible formats.
- **Voice Selection Logic:** Created configuration options for different voice personas based on message context and user preferences.

### Learnings / Outcomes
- Gained hands-on experience with AWS SDK for Python (boto3) and audio processing pipelines.
- Successfully generated and played synthesized speech responses in Teams test environment.

### Blockers / Risks
- Initial challenges with audio format compatibility between AWS Polly and Teams, resolved through format conversion.

### Skills Used
AWS Polly, boto3, Audio Processing, Stream Management, Text-to-Speech APIs, Media Format Conversion

## Tuesday, February 10th, 2026

### What I worked on?
- **Database Schema Design:** Designed MongoDB schemas for storing task information, sprint data, and conversation history.
- **Connection Pool Setup:** Configured MongoDB connection pooling for efficient database operations at scale.
- **CRUD Operations:** Implemented Create, Read, Update, and Delete operations for task management functionality.

### Learnings / Outcomes
- Learned MongoDB best practices for schema design in document-oriented databases.
- Successfully established reliable database connectivity with proper error handling and retry logic.

### Blockers / Risks
- *None reported today.*

### Skills Used
MongoDB, Database Schema Design, Connection Pooling, PyMongo, CRUD Operations, Error Handling

## Wednesday, February 11th, 2026

### What I worked on?
- **Natural Language Processing:** Integrated spaCy for NLP to better understand and parse user intentions from natural language inputs.
- **Intent Recognition:** Developed intent classification system to categorize user messages into scrum-related actions.
- **Entity Extraction:** Implemented named entity recognition to extract task details, assignees, and deadlines from conversations.

### Learnings / Outcomes
- Mastered spaCy's pipeline architecture and custom entity recognition training.
- Achieved 85% accuracy in intent classification for common scrum-related queries.

### Blockers / Risks
- *None reported today.*

### Skills Used
spaCy, Natural Language Processing, Intent Classification, Named Entity Recognition, Machine Learning Pipeline

## Thursday, February 12th, 2026

### What I worked on?
- **Task State Management:** Built a state machine to track task lifecycle from creation through completion with proper status transitions.
- **Conversation Context:** Implemented conversation context management to maintain continuity across multiple bot interactions.
- **Session Persistence:** Developed session storage mechanism to preserve user context between Teams sessions.

### Learnings / Outcomes
- Learned the importance of state management in conversational AI and its impact on user experience.
- Successfully maintained conversation context across bot restarts and deployments.

### Blockers / Risks
- *None reported today.*

### Skills Used
State Machine Design, Redis Cache, Session Management, Context Preservation, Distributed Systems

## Friday, February 13th, 2026

### What I worked on?
- **Sprint Planning Features:** Developed sprint planning capabilities allowing teams to create, modify, and track sprints through bot commands.
- **Velocity Calculations:** Implemented story point tracking and velocity calculations for sprint performance metrics.
- **Burndown Generation:** Created automated burndown chart generation using matplotlib for visual sprint progress tracking.

### Learnings / Outcomes
- Gained insights into agile metrics and their importance in team productivity tracking.
- Successfully generated and embedded burndown charts in Teams messages using Adaptive Cards.

### Blockers / Risks
- *None reported today.*

### Skills Used
Agile Metrics, matplotlib, Data Visualization, Sprint Management, Story Point Calculations, Chart Generation

## Monday, February 16th, 2026

### What I worked on?
- **Docker Containerization:** Containerized the Python bot application using Docker for consistent deployment across environments.
- **Multi-stage Build:** Implemented multi-stage Docker builds to optimize image size and separate build dependencies from runtime.
- **Environment Configuration:** Set up environment-specific configuration management using Docker environment variables and secrets.

### Learnings / Outcomes
- Mastered Docker best practices for Python applications including layer caching and security scanning.
- Reduced final Docker image size by 60% through multi-stage build optimization.

### Blockers / Risks
- *None reported today.*

### Skills Used
Docker, Containerization, Multi-stage Builds, Environment Variables, Container Security, Image Optimization

## Tuesday, February 17th, 2026

### What I worked on?
- **Google Cloud Setup:** Configured Google Cloud project with necessary APIs enabled for Container Registry and Cloud Run deployment.
- **Service Account Creation:** Created and configured service accounts with appropriate IAM roles for automated deployments.
- **Container Registry Push:** Successfully pushed Docker images to Google Container Registry with proper tagging strategy.

### Learnings / Outcomes
- Learned GCP's approach to container orchestration and serverless deployment options.
- Established secure CI/CD pipeline for automated container deployments.

### Blockers / Risks
- Initial authentication issues with service account keys, resolved through proper IAM configuration.

### Skills Used
Google Cloud Platform, Container Registry, IAM Configuration, Service Accounts, Cloud Run, GCP CLI

## Wednesday, February 18th, 2026

### What I worked on?
- **Cloud Run Deployment:** Deployed the containerized bot to Google Cloud Run with auto-scaling configuration.
- **HTTPS Endpoint Setup:** Configured secure HTTPS endpoints with managed SSL certificates for bot webhook communication.
- **Environment Variables:** Migrated all sensitive configuration to Cloud Run environment variables and Google Secret Manager.

### Learnings / Outcomes
- Understood the advantages of serverless architecture for event-driven bot applications.
- Successfully achieved sub-second cold start times through container optimization.

### Blockers / Risks
- *None reported today.*

### Skills Used
Cloud Run, Serverless Architecture, SSL/TLS Configuration, Secret Management, Auto-scaling, Webhook Configuration

## Thursday, February 19th, 2026

### What I worked on?
- **Performance Monitoring:** Integrated Google Cloud Monitoring to track bot response times and resource utilization.
- **Logging Pipeline:** Set up structured logging with Cloud Logging for debugging and audit trails.
- **Alert Configuration:** Created alerting rules for service degradation and error rate thresholds.

### Learnings / Outcomes
- Learned the importance of observability in production systems and proactive monitoring.
- Identified and resolved a memory leak through detailed performance metrics analysis.

### Blockers / Risks
- *None reported today.*

### Skills Used
Cloud Monitoring, Structured Logging, Performance Analysis, Alert Management, Observability, Debugging

## Friday, February 20th, 2026

### What I worked on?
- **Load Testing:** Conducted load testing using Locust to simulate concurrent Teams users interacting with the bot.
- **Rate Limiting:** Implemented rate limiting to prevent API abuse and ensure fair resource usage across teams.
- **Caching Strategy:** Developed Redis-based caching layer to reduce database queries for frequently accessed data.

### Learnings / Outcomes
- Discovered optimal scaling parameters through load testing, supporting 500 concurrent users.
- Reduced average response time by 40% through strategic caching implementation.

### Blockers / Risks
- *None reported today.*

### Skills Used
Locust, Load Testing, Rate Limiting, Redis Caching, Performance Optimization, Scalability Testing

## Saturday, February 21st, 2026

### What I worked on?
- **Weekend Deployment:** Executed production deployment during maintenance window with zero-downtime strategy.
- **Rollback Plan Testing:** Tested rollback procedures to ensure quick recovery in case of deployment issues.
- **Documentation Update:** Updated deployment runbooks and operational procedures based on deployment experience.

### Learnings / Outcomes
- Successfully completed first production deployment with all stakeholders informed and prepared.
- Validated the importance of comprehensive rollback plans and documentation.

### Blockers / Risks
- *None reported today.*

### Skills Used
Production Deployment, Zero-downtime Deployment, Rollback Strategies, Documentation, Change Management

## Sunday, February 22nd, 2026

### What I worked on?
- **Post-Deployment Monitoring:** Monitored production metrics following yesterday's deployment to ensure system stability.
- **User Feedback Analysis:** Analyzed initial user feedback and identified areas for UX improvements in bot interactions.
- **Bug Triage:** Prioritized and documented minor issues discovered during initial production usage.

### Learnings / Outcomes
- Learned the value of post-deployment monitoring and rapid response to user feedback.
- Identified three UX improvements that will significantly enhance user satisfaction.

### Blockers / Risks
- *None reported today.*

### Skills Used
Production Monitoring, User Feedback Analysis, Bug Triage, UX Assessment, Incident Response

## Monday, February 23rd, 2026

### What I worked on?
- **MongoDB Integration:** Implemented response logging infrastructure using MongoDB to track bot interactions and conversation history.
- **Database Schema Design:** Created optimized document schemas for storing Teams conversation states, user queries, and AI responses with timestamps.
- **Logging Middleware Setup:** Developed Python middleware to intercept bot responses and persist them asynchronously to the MongoDB cluster.

### Learnings / Outcomes
- Learned how to efficiently handle high-volume write operations in MongoDB using bulk insert operations.
- Successfully established persistent conversation tracking that will enable advanced analytics and debugging capabilities.

### Blockers / Risks
- *None reported today.*

### Skills Used
MongoDB, Database Schema Design, Python Middleware, Asynchronous Programming, Document Databases, Response Logging, Data Persistence

## Tuesday, February 24th, 2026

### What I worked on?
- **Role-Based Access Control:** Modified the database schema to introduce a hierarchical role system with scrum master privileges for task management.
- **Task Assignment Data Model:** Designed new collection structures to support dynamic task assignment with owner tracking, delegation history, and role-based permissions.
- **Schema Migration Strategy:** Implemented versioned migration scripts to safely evolve the existing database structure without disrupting active bot sessions.

### Learnings / Outcomes
- Mastered MongoDB schema evolution patterns including backward-compatible field additions and index optimization for role-based queries.
- Successfully implemented a flexible RBAC system that differentiates between team members, scrum masters, and product owners.

### Blockers / Risks
- *None reported today.*

### Skills Used
Database Migration, Role-Based Access Control (RBAC), MongoDB Schema Evolution, Task Assignment Modeling, Permission Systems, Data Model Versioning

## Wednesday, February 25th, 2026

### What I worked on?
- **Task Assignment Card UI:** Built card components with task assignment fields, user selection dropdowns, and action buttons enabling scrum masters to delegate tasks directly.
- **Frontend User Handlers:** Implemented frontend handler logic to process user interactions, validate task assignment inputs, and relay assignment data to the backend API.
- **Scrum Master Assignment Flow:** Developed the end-to-end workflow allowing scrum masters to view pending tasks, assign them to team members, and track delegation through the card interface.

### Learnings / Outcomes
- Gained hands-on experience building interactive card-based UIs with dynamic user selection and task delegation capabilities.
- Successfully delivered a functional task assignment flow that streamlines the scrum master's ability to distribute work across the team.

### Blockers / Risks
- *None reported today.*

### Skills Used
Frontend Development, Card UI Components, Event Handling, Task Assignment Logic, User Interface Design, API Integration, Python, Bot Framework SDK

## Thursday, February 26th, 2026

### What I worked on?
- **Unit Test Suite Development:** Created comprehensive unit tests for the task assignment feature covering scrum master permissions, member restrictions, and edge cases.
- **Integration Testing:** Tested end-to-end task assignment flow between Teams interface, bot backend, and MongoDB to verify data persistence and role validation.
- **Role-Based Test Scenarios:** Executed test cases for different user roles, ensuring scrum masters can assign tasks while regular members receive appropriate access denied messages.

### Learnings / Outcomes
- Discovered and fixed a critical bug where task reassignments weren't updating the delegation history correctly.
- Achieved 95% code coverage for the task assignment module with all tests passing successfully.

### Blockers / Risks
- *None reported today.*

### Skills Used
Unit Testing, Integration Testing, pytest, Test Coverage Analysis, Bug Detection, Teams Bot Testing, Role-Based Testing, Test Automation

## Friday, February 27th, 2026

### What I worked on?
- **End-to-End Validation Framework:** Designed comprehensive E2E test scenarios validating the complete workflow from Teams user interaction through bot processing to MongoDB persistence and response rendering.
- **Cross-Component Data Integrity:** Implemented validation checks ensuring data consistency across all system layers including Teams metadata, bot context, API payloads, and database records.
- **Performance Benchmarking:** Conducted load testing with multiple concurrent users to validate system response times and identify bottlenecks in the task assignment pipeline.

### Learnings / Outcomes
- Identified and resolved race conditions occurring when multiple scrum masters attempted simultaneous task assignments.
- Established baseline performance metrics showing sub-2 second response times for complete task assignment workflows.

### Blockers / Risks
- *None reported today.*

### Skills Used
End-to-End Testing, Data Validation, Performance Testing, Load Testing, System Integration Validation, Race Condition Detection, Workflow Testing, Benchmark Analysis

## Saturday, February 28th, 2026

### What I worked on?
- **Concurrency Control Implementation:** Implemented mutex locks and database-level transactions to permanently resolve the race condition issues discovered during E2E testing.
- **Code Refactoring & Optimization:** Refactored the task assignment module for better maintainability, extracting common patterns and removing code duplication.
- **Pull Request Preparation:** Prepared the feature branch for merge by updating documentation, cleaning up debug statements, and ensuring all linting standards were met.

### Learnings / Outcomes
- Successfully implemented thread-safe concurrent task assignment handling using Python's threading locks and MongoDB transactions.
- Reduced the task assignment codebase by 15% through strategic refactoring while maintaining all functionality and test coverage.

### Blockers / Risks
- *None reported today.*

### Skills Used
Concurrency Control, Mutex Implementation, Database Transactions, Code Refactoring, Pull Request Management, Code Review Preparation, Python Threading, MongoDB Transactions

## Sunday, March 1st, 2026

### What I worked on?
- **Technical Documentation Update:** Wrote comprehensive API documentation for the task assignment module, detailing endpoint specifications, request/response formats, and role-based access rules.
- **Sprint Retrospective Notes:** Compiled retrospective notes for the completed sprint, highlighting the successful delivery of the task assignment feature and identifying process improvements for the next iteration.
- **Code Review Preparation:** Reviewed the pull request diff for the task assignment feature, adding clarifying comments and ensuring all team review guidelines were met before Monday's review session.

### Learnings / Outcomes
- Learned the importance of clear API documentation in facilitating team collaboration and future maintenance.
- Identified two process improvements from the retrospective that could reduce development cycle time by 20%.

### Blockers / Risks
- *None reported today.*

### Skills Used
Technical Writing, API Documentation, Sprint Retrospective, Code Review, Markdown Documentation, Process Analysis, Knowledge Sharing

## Monday, March 2nd, 2026

### What I worked on?
- **Standup Feature Requirements Gathering:** Analyzed business requirements for automated daily standup meetings, identifying key features like scheduled triggers, participant tracking, and report generation.
- **Meeting Flow Architecture Design:** Designed the standup bot conversation flow including question prompts, response collection, timeout handling, and summary compilation strategies.
- **Teams Meeting API Research:** Investigated Microsoft Graph API capabilities for scheduling recurring meetings, managing participants, and integrating standup reports into Teams channels.

### Learnings / Outcomes
- Discovered Microsoft Graph API's powerful meeting orchestration capabilities that can automate standup scheduling and participant management.
- Identified the optimal architecture pattern using Azure Functions for scheduled triggers combined with the existing bot framework for interactive elements.

### Blockers / Risks
- *None reported today.*

### Skills Used
Requirements Analysis, Flow Design, Microsoft Graph API, Meeting Automation, System Architecture Planning, Azure Functions, Conversation Design

## Tuesday, March 3rd, 2026

### What I worked on?
- **Graph API SDK Deep Dive:** Studied Microsoft Graph Python SDK documentation, exploring authentication patterns, batch request optimization, and delta query mechanisms for efficient participant tracking.
- **Bot State Machine Specification:** Detailed the standup bot's state transitions including idle, question-asking, awaiting-response, timeout-handling, and summary-generation states with precise transition triggers.
- **Data Model Planning:** Designed MongoDB schemas for standup sessions, participant responses, and aggregated reports, ensuring compatibility with existing task assignment collections.

### Learnings / Outcomes
- Discovered Graph API's delta queries can significantly reduce API calls by tracking only changes in meeting participants.
- Identified potential state machine complexity that will require careful testing of edge cases like mid-standup disconnections.

### Blockers / Risks
- *None reported today.*

### Skills Used
Microsoft Graph SDK, State Machine Design, MongoDB Schema Planning, API Documentation Analysis, Delta Queries, Python SDK Integration, Data Model Architecture

## Wednesday, March 4th, 2026

### What I worked on?
- **Voice Standup Initialization:** Implemented the core state machine logic for managing the automated voice standups flow.
- **Audio Prompt Integration:** Integrated AWS Polly to dynamically generate spoken prompts for daily standup questions.
- **Participant Orchestration:** Set up Microsoft Graph API integration to coordinate meeting participants and track active speakers.

### Learnings / Outcomes
- Successfully translated the previously specified state machine design into functional Python bot logic.
- Managed to achieve smooth synchronization between audio playback states and user input transitions.

### Blockers / Risks
- *None reported today.*

### Skills Used
State Machine Implementation, AWS Polly, Microsoft Graph API, Audio Synchronization, Python Bot Framework

## Thursday, March 5th, 2026

### What I worked on?
- **Feature Scaffolding:** Set up the directory structure and foundational module files for the new automated voice standup feature.
- **Dependency Integration:** Configured necessary library dependencies, integrating the Microsoft Graph SDK and AWS boto3 into the module's environment.
- **State Machine Framework:** Stubbed out the core classes and routing methods for the standup bot's state transitions based on the previous days' designs.

### Learnings / Outcomes
- Gained practical experience in structurally organizing a complex new feature within an existing application architecture.
- Learned the importance of clean module separation when preparing to integrate diverse external APIs like Microsoft Graph and AWS Polly.

### Blockers / Risks
- *None reported today.*

### Skills Used
Project Scaffolding, Software Architecture, Module Organization, Python, API Integration Planning

## Friday, March 6th, 2026

### What I worked on?
- **Participant Roll Call Logic:** Implemented the Microsoft Graph API integration to dynamically fetch active meeting participants and initialize the standup roster.
- **Audio Stream Pipeline:** Developed the AWS Polly text-to-speech pipeline to synthesize and stream audio prompts directly into the Teams call.
- **State Machine Integration:** Connected the participant fetcher and audio pipeline to the core state machine, fully activating the 'initialization' and 'question-asking' states.

### Learnings / Outcomes
- Mastered handling asynchronous API calls to Microsoft Graph and managing pagination for large meeting rosters within the bot's state transitions.
- Gained a deep understanding of the specific audio streaming formats and buffer management required by the Teams Bot Framework for seamless voice playback.

### Blockers / Risks
- *None reported today.*

### Skills Used
Python Async/Await, AWS Polly Streaming, Microsoft Graph API, Audio Format Conversion, Bot Framework SDK

## Saturday, March 7th, 2026

### What I worked on?
- **Code Refactoring & Cleanup:** Refactored the voice standup modules to improve maintainability, cleanly separating the Microsoft Graph API and AWS Polly logic into reusable helper classes.
- **Unit Test Implementation:** Developed unit tests to validate the new state machine transitions, utilizing mock objects for external AWS and Graph API responses.
- **Feature Documentation:** Drafted technical documentation detailing the automated voice standup architecture, state transition triggers, and necessary environment configurations.

### Learnings / Outcomes
- Reinforced best practices in modular code design by successfully decoupling external service dependencies from the bot's core state logic.
- Established solid baseline test coverage for the initial standup phases, ensuring robust error handling when simulating API failures.

### Blockers / Risks
- *None reported today.*

### Skills Used
Code Refactoring, Unit Testing, pytest, API Mocking, Technical Documentation

## Sunday, March 8th, 2026

### What I worked on?
- **Sprint Retrospective:** Compiled notes on the automated voice standup feature development, analyzing the integration challenges with Microsoft Graph and AWS Polly.
- **Sprint Planning Preparation:** Outlined the remaining tasks and bug fixes needed to complete the standup module for the upcoming week.
- **Documentation Review:** Reviewed and polished the technical documentation generated yesterday, ensuring the state machine flow is clear for the broader team.

### Learnings / Outcomes
- Identified that earlier prototyping of external API connections (like Graph API) can significantly streamline the main development phase.
- Structured a clear task list for the upcoming sprint, ensuring a seamless handover and code review process.

### Blockers / Risks
- *None reported today.*

### Skills Used
Sprint Retrospective, Sprint Planning, Technical Documentation Review, Agile Processes, Project Management

## Monday, March 9th, 2026

### What I worked on?
- **Azure ACS Provisioning:** Provisioned the Azure Communication Services (ACS) resource within the Azure portal to support advanced voice calling capabilities.
- **Access Keys Configuration:** Configured secure connection strings and access keys to link the new ACS resource with the existing Bot Framework deployment.
- **Identity Token Generation Prep:** Researched the ACS identity SDK to prepare for generating user access tokens required for initiating voice standup calls.

### Learnings / Outcomes
- Understood the foundational role of Azure Communication Services in enabling direct Voice-over-IP (VoIP) and PSTN calling within Teams bot architectures.
- Learned how to properly secure and manage ACS access credentials within the project's cloud environment.

### Blockers / Risks
- *None reported today.*

### Skills Used
Azure Communication Services (ACS), Resource Provisioning, Cloud Security, API Key Management, Azure Portal

## Tuesday, March 10th, 2026

### What I worked on?
- **ACS Identity Integration:** Implemented the Azure Communication Services Identity SDK to generate user identities.
- **Access Token Generation:** Developed logic to issue access tokens with necessary calling scopes for the bot.
- **Bot Framework Configuration:** Injected the generated ACS identity tokens into the bot framework's startup sequence.

### Learnings / Outcomes
- Learned how to securely authenticate ACS users programmatically to enable VoIP communications.
- Successfully managed token lifecycles and scopes required for Teams call interoperability.

### Blockers / Risks
- *None reported today.*

### Skills Used
Azure Identity SDK, Token Management, VoIP Authentication, Python Integration

## Wednesday, March 11th, 2026

### What I worked on?
- **Speech Resource Configuration:** Provisioned and configured the Azure Cognitive Speech service resource in the Azure portal.
- **Service Integration:** Linked the new cognitive speech resource with the existing Azure Communication Services (ACS).
- **IAM Policy Setup:** Configured Identity and Access Management (IAM) policies to ensure secure interoperability between the services.

### Learnings / Outcomes
- Gained practical experience in connecting multiple Azure services using secure identity configurations.
- Understood the IAM requirements for integrating cognitive speech capabilities into an ACS-driven voice application.

### Blockers / Risks
- *None reported today.*

### Skills Used
Azure Cognitive Services, Azure Communication Services (ACS), IAM (Identity and Access Management), Cloud Resource Configuration, System Integration

## Thursday, March 12th, 2026

### What I worked on?
- **Adaptive Card Design:** Drafted the JSON schemas for the interactive Microsoft Teams cards used in the voice standup feature.
- **Action Button Integration:** Added specific action buttons to the cards to trigger the automated voice standup calls.
- **Bot Framework Payload Setup:** Configured the bot framework to construct and send the designed adaptive card payloads dynamically.

### Learnings / Outcomes
- Understood the JSON structure required to build and render Adaptive Cards within Microsoft Teams.
- Learned how to seamlessly connect UI interactions within Teams to backend voice automation triggers.

### Blockers / Risks
- *None reported today.*

### Skills Used
Adaptive Cards, JSON, UI/UX Design, Microsoft Teams Integration, Azure Bot Framework
