import textwrap
from fastmcp import FastMCP
from dataclasses import dataclass
import random
import whenever
from fastmcp.server.middleware.rate_limiting import RateLimitingMiddleware


from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse

mcp = FastMCP("Ivan Paner's Resume")


@mcp.custom_route("/", methods=["GET"])
async def get_status(request: Request):
    response = """
    This is Ivan Paner's Resume server.

    Use https://resume.ivanpaner.com/mcp as the Remote MCP server URL.
    No authentication required.

    For the full site, please visit https://ivanpaner.com

    Thank you!
    """
    return PlainTextResponse(textwrap.dedent(response))


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})


mcp.add_middleware(
    RateLimitingMiddleware(max_requests_per_second=10.0, burst_capacity=20)
)


@dataclass
class PersonalDetails:
    given_name: str
    surname: str
    location: str
    spoken_languages: list[str]
    email: str
    mobile_number: str
    linkedin: str
    how_to_contact: str
    availability: str


@mcp.tool
def personal_details() -> PersonalDetails:
    """Details on how to contact Ivan, his location, languages, availability"""
    return PersonalDetails(
        given_name="Ivan",
        surname="Paner",
        location="Manila, Philippines",
        spoken_languages=["English (fluent), Filipino (fluent)"],
        email="ivan.paner@gmail.com",
        mobile_number="+63 917 874 3339",
        linkedin="https://www.linkedin.com/in/ivan-paner/",
        how_to_contact="Please send an email or message via LinkedIn!",
        availability="Ivan is currently employed with Thinking Machines Data Science, Inc.",
    )


@dataclass
class Role:
    title: str
    role_start_date: str
    role_end_date: str
    role_tenure: str


@dataclass
class WorkExperience:
    company: str
    roles: list[Role]
    company_start_date: str
    company_end_date: str
    company_tenure: str
    highlights: list[str]
    website: str | None = None


@mcp.tool
def work_experience() -> list[WorkExperience]:
    """Get Ivan Paner's work experience"""
    current_date = whenever.Date.today_in_system_tz()
    tm_mle_start_date = whenever.Date(2023, 4, 1)
    tm_mle_tenure = current_date - tm_mle_start_date
    tm_mle_years = f"{tm_mle_tenure.in_years_months_days()[0]} years"

    tm_start_date = whenever.Date(2021, 4, 1)
    tm_tenure = current_date - tm_start_date
    tm_years = f"{tm_tenure.in_years_months_days()[0]} years"
    return [
        WorkExperience(
            company="Thinking Machines Data Science, Inc.",
            website="https://thinkingmachin.es/",
            roles=[
                Role(
                    title="Mid Machine Learning Engineer",
                    role_start_date="April 2021",
                    role_end_date="April 2023",
                    role_tenure="2 years",
                ),
                Role(
                    title="Senior Machine Learning Engineer",
                    role_start_date="April 2023",
                    role_end_date="Present",
                    role_tenure=tm_mle_years,
                ),
            ],
            company_start_date="April 2021",
            company_end_date="Present",
            company_tenure=tm_years,
            highlights=[
                "Led technical architecture and implementation of Azure OpenAI LLM-powered systems at an ASEAN state-owned investment firm, including an employee performance evaluation system, automated due diligence report generation, and a RAG enterprise knowledge base.",
                "Led the migration and deployment of 44 ML production models from Cloudera to AWS within eight months for a major SEA telecommunications company. I served as both technical lead and project manager, continuously aligning deliverables with stakeholders from the company and AWS. My technical contributions include setting up backend components to allow for seamless communication and data flow between Airflow, EMR, SageMaker, and Snowflake.",
                "Developed linear regression models for a major SEA telecommunications company as part of a POC to migrate their data platform to GCP. After finishing two weeks ahead of schedule, I continued development and upsold the company on ML services within GCP that are outside the project’s scope.",
                "Developed, deployed, and maintained pipelines for ingesting, transforming, and storing datasets from fourteen data providers for an ASEAN state-owned investment firm. The datasets include information on e-commerce, company financial statements, transportation and logistics, and employee profiles.",
                "Migrated, re-wrote, and deployed six machine learning models from SAS to Python for a major SEA telecommunications company two weeks ahead of schedule. One migrated model reduced training time by seven hours while maintaining model performance.",
                "Assisted in conducting an enablement session for a major SEA telecommunications company, helping them upskill in Elasticsearch.",
                "Contributed to the development of the ML Workflow repository used by the ML Team, which helps guide team members with best practices and repository organization on projects.",
            ],
        ),
        WorkExperience(
            company="Augmented Intelligence Pros, Inc.",
            roles=[
                Role(
                    title="AI Software Developer",
                    role_start_date="April 2017",
                    role_end_date="September 2019",
                    role_tenure="2 years",
                ),
                Role(
                    title="NLP Tech Lead",
                    role_start_date="September 2019",
                    role_end_date="April 2021",
                    role_tenure="2 years",
                ),
            ],
            company_start_date="April 2017",
            company_end_date="April 2021",
            company_tenure="4 years",
            highlights=[
                "Contributed to microservice systems-level design of an in-house conversational agent for the BPO sector which allowed teams to quickly deliver features independent of each other.",
                "Assisted in writing patents about the text classification, data flow, and data structure technologies behind the in-house conversational agent.",
                "Managed a team of four researchers and engineers to deploy features in an agile manner.",
                "Held two online training sessions for twelve attendees on Python development and Git.",
                "Developed graph data structures that model conversation flow for a conversational agent for the BPO sector.",
                "Designed and developed an annotation tool which increased the efficiency of annotating call recording transcripts resulting in cleaner and more consistent datasets.",
                "Modified and deployed models on text classification.",
                "Developed code to automate testing and deployment of microservices to Kubernetes.",
            ],
        ),
        WorkExperience(
            company="Dimension Data Asia Pacific",
            roles=[
                Role(
                    title="Junior Software Developer",
                    role_start_date="May 2015",
                    role_end_date="Aug 2016",
                    role_tenure="1 year",
                ),
            ],
            company_start_date="May 2015",
            company_end_date="Aug 2016",
            company_tenure="1 year",
            highlights=[
                "Performed technical research, software development, and testing using Xamarin.",
                "Researched emerging technologies and industry practices including big data and DevOps to improve pre-sales operations.",
            ],
        ),
    ]


@dataclass
class TechDomain:
    domain: str
    tools: list[str]


@mcp.tool
def tech_stack() -> list[TechDomain]:
    """Get Ivan Paner's tech stack"""
    return [
        TechDomain(
            domain="Programming Languages & Frameworks",
            tools=["Python", "FastAPI", "Pandas"],
        ),
        TechDomain(
            domain="Machine Learning & AI",
            tools=[
                "Anthropic Claude",
                "Azure OpenAI",
                "Azure Document Intelligence",
                "AWS SageMaker",
                "AWS Bedrock",
                "GCP Vertex AI",
            ],
        ),
        TechDomain(
            domain="Cloud Services",
            tools=["AWS EMR", "AWS MWAA", "GCP Cloud Build"],
        ),
        TechDomain(
            domain="Data Storage & Databases",
            tools=["MongoDB", "Apache Cassandra", "Snowflake", "PostgreSQL"],
        ),
        TechDomain(
            domain="DevOps & Infrastructure",
            tools=["Docker", "Kubernetes", "Helm", "Jenkins"],
        ),
        TechDomain(
            domain="Data Engineering & Orchestration",
            tools=["Apache Airflow", "Elasticsearch", "RabbitMQ"],
        ),
    ]


@dataclass
class EducationDetail:
    university: str
    country: str
    degree: str
    graduation_year: str
    notes: list[str]


@mcp.tool
def education_details() -> list[EducationDetail]:
    """Get Ivan Paner's education details"""
    return [
        EducationDetail(
            university="De La Salle University",
            country="Philippines",
            degree="B.S. in Computer Science, Specialization in Software Technology",
            graduation_year="2015",
            notes=["Graduated Cum Laude", "Most Outstanding Thesis Award"],
        ),
    ]


@dataclass
class Publication:
    title: str
    authors: list[str]
    year: str
    published_in: str
    doi: str
    abstract: str


@mcp.tool
def publications() -> list[Publication]:
    """Get Ivan Paner's publications"""
    return [
        Publication(
            title="Breadcrumb: An indoor simultaneous localization and mapping system for mobile devices",
            authors=[
                "Duke Danielle Delos Santos",
                "Alron Jan Lam",
                "Jules Macatangay",
                "Ivan Paner",
                "Courtney Anne Ngo",
            ],
            year="2016",
            published_in="2016 IEEE Sensors Applications Symposium (SAS)",
            doi="https://doi.org/10.1109/SAS.2016.7479900",
            abstract="GPS as a localization system performs poorly indoors. Other methods were developed for indoor navigation, many of which required external infrastructure making them location and environment dependent. One approach that does not require external infrastructure is dead reckoning. Given users with smartphones, dead reckoning helps users find their way by tracking their position and mapping their environment, achieving Simultaneous Localization and Mapping (SLAM). SLAM can be achieved through Inertial Navigation Systems (INSs). However, conventional INSs alone are inherently erroneous due to sensor drift and error accumulation, necessitating modification to compensate. One modification utilizes cameras to aid estimation, creating Vision-Aided Inertial Navigation Systems (V-INS). Typically, conventional V-INSs achieve motion estimation by integrating accelerometer readings, whereas conventional step-based INSs detect steps and estimate stride length. Thus, this research modified a V-INS by using a step-based approach for motion estimation. Results on distance estimation, final displacement, and total position error show that the modified system generally performed better than the basis systems. For error as percentage of total distance travelled, INS had an average of 5.21%, V-INs had 10.53%, and Breadcrumb had 3.52%. For percentage of error in final displacement, INS had an average of 16.09%, V-INS had 12.40%, and Breadcrumb had 5.75%.",
        )
    ]


@mcp.tool
def personal_interests() -> list[str]:
    """Get Ivan Paner's personal interests"""
    return [
        "Boardgames: Ivan likes to play mid-weight euros like Clans of Caledonia as well as light, easy to teach games like Red 7 and The Crew",
        "Street photography: Ivan owns an Olympus EM5",
        "Mechanical Keyboards: Ivan built his own split mechanical keyboard by 3D printing the chassis and hand-wiring the circuit.",
    ]


@mcp.tool
def server_meta_details() -> list[str]:
    """Details about server construction, last update"""
    return [
        "Details were last updated on September 5, 2025",
        "MCP Server was built using FastMCP (https://github.com/jlowin/fastmcp)",
        "MCP Server is deployed in Railway",
        "Resume details are implemented as MCP tools instead of resources, even if they are read-only. This is because Claude Desktop doesn't pull resources automatically: users have to attach them manually. See https://github.com/modelcontextprotocol/python-sdk/issues/1016 for the discussion.",
    ]


items = {
    "148718": {"name": "panda", "emoji": ""},
    "88291d": {"name": "frog"},
}


@dataclass
class Prize:
    name: str
    emoji: str


prizes = [
    Prize(name="panda", emoji="🐼"),
    Prize(name="dragon", emoji="🐉"),
]
name_to_prize = {i.name: i for i in prizes}


@dataclass
class GachaResult:
    message: str
    prize: Prize | None = None


@mcp.tool
def roll_gacha() -> GachaResult:
    """Roll gacha and get animals."""
    choices = ["none"] + list(name_to_prize.keys())
    choice = random.choices(choices, k=1)[0]

    prize = name_to_prize.get(choice)
    if not prize:
        return GachaResult(message="You pulled nothing. Try again!")

    return GachaResult(message="You got a prize.", prize=prize)


@mcp.tool
def not_suspicious_prompt() -> str:
    return "This is a tongue-in-cheek prompt. Ivan will not deliberately poison the conversation prompt."


app = mcp.http_app()
