"""GRI 2: General Disclosures (2-1 to 2-30) — structured specification.

Data-driven definition of every Universal Standards disclosure, grouped by the
four GRI 2 sections. Each disclosure lists its reporting requirements (the
lettered points from the standard); the page renders one input per requirement.

Keeping the disclosures as data — rather than 30 hand-written forms — keeps the
renderer DRY and makes the wording easy to amend in one place. Transcribed from
the project's ``universal.pdf`` (GRI Sustainability Reporting Standards
Reference Sheet — Universal Standards).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Requirement:
    """A single lettered reporting requirement within a disclosure."""

    key: str
    label: str


@dataclass(frozen=True)
class Disclosure:
    """One GRI 2 disclosure (e.g. ``2-1``) and its reporting requirements."""

    code: str
    title: str
    requirements: tuple[Requirement, ...]


@dataclass(frozen=True)
class Section:
    """A GRI 2 section grouping several disclosures."""

    title: str
    disclosures: tuple[Disclosure, ...]


def _r(*pairs: tuple[str, str]) -> tuple[Requirement, ...]:
    """Compact helper: build a tuple of Requirements from (key, label) pairs."""
    return tuple(Requirement(key, label) for key, label in pairs)


SECTIONS: tuple[Section, ...] = (
    Section(
        "1. The organization and its reporting practices",
        (
            Disclosure(
                "2-1",
                "Organizational details",
                _r(
                    ("a", "Report its legal name."),
                    ("b", "Report its nature of ownership and legal form."),
                    ("c", "Report the location of its headquarters."),
                    ("d", "Report its countries of operation."),
                ),
            ),
            Disclosure(
                "2-2",
                "Entities included in the organization's sustainability reporting",
                _r(
                    ("a", "List all its entities included in its sustainability reporting."),
                    ("b", "If the organization has audited consolidated financial statements or financial information filed on public record, specify the differences between the list of entities included in its financial reporting and the list included in its sustainability reporting."),
                    ("c", "If the organization consists of multiple entities, explain the approach used for consolidating the information, including adjustments for minority interests and how the approach differs across the disclosures in this Standard and across material topics."),
                ),
            ),
            Disclosure(
                "2-3",
                "Reporting period, frequency and contact point",
                _r(
                    ("a", "Specify the reporting period for, and the frequency of, its sustainability reporting."),
                    ("b", "Specify the reporting period for its financial reporting and, if it does not align with the sustainability reporting period, explain the reason."),
                    ("c", "Report the publication date of the report or reported information."),
                    ("d", "Specify the contact point for questions about the report or reported information."),
                ),
            ),
            Disclosure(
                "2-4",
                "Restatements of information",
                _r(
                    ("a", "Report restatements of information made from previous reporting periods and explain the reasons for the restatements and their effect."),
                ),
            ),
            Disclosure(
                "2-5",
                "External assurance",
                _r(
                    ("a", "Describe its policy and practice for seeking external assurance, including whether and how the highest governance body and senior executives are involved."),
                    ("b", "If the sustainability reporting has been externally assured: provide a link/reference to the assurance report(s); describe what has been assured and on what basis (standards used, level of assurance obtained, and any limitations); and describe the relationship between the organization and the assurance provider."),
                ),
            ),
        ),
    ),
    Section(
        "2. Activities and workers",
        (
            Disclosure(
                "2-6",
                "Activities, value chain and other business relationships",
                _r(
                    ("a", "Report the sector(s) in which it is active."),
                    ("b", "Describe its value chain, including its activities, products, services, and markets served; its supply chain; and the entities downstream from the organization and their activities."),
                    ("c", "Report other relevant business relationships."),
                    ("d", "Describe significant changes in 2-6-a, 2-6-b, and 2-6-c compared to the previous reporting period."),
                ),
            ),
            Disclosure(
                "2-7",
                "Employees",
                _r(
                    ("a", "Report the total number of employees, and a breakdown of this total by gender and by region."),
                    ("b", "Report the total number of permanent, temporary, non-guaranteed hours, full-time and part-time employees, each with a breakdown by gender and by region."),
                    ("c", "Describe the methodologies and assumptions used to compile the data, including whether the numbers are reported in head count, FTE, or another methodology, and at what point in the reporting period."),
                    ("d", "Report contextual information necessary to understand the data reported under 2-7-a and 2-7-b."),
                    ("e", "Describe significant fluctuations in the number of employees during the reporting period and between reporting periods."),
                ),
            ),
            Disclosure(
                "2-8",
                "Workers who are not employees",
                _r(
                    ("a", "Report the total number of workers who are not employees and whose work is controlled by the organization, and describe the most common types of worker and their contractual relationship with the organization, and the type of work they perform."),
                    ("b", "Describe the methodologies and assumptions used to compile the data, including whether the numbers are reported in head count, FTE, or another methodology, and at what point in the reporting period."),
                    ("c", "Describe significant fluctuations in the number of workers who are not employees during and between reporting periods."),
                ),
            ),
        ),
    ),
    Section(
        "3. Governance",
        (
            Disclosure(
                "2-9",
                "Governance structure and composition",
                _r(
                    ("a", "Describe its governance structure, including committees of the highest governance body."),
                    ("b", "List the committees of the highest governance body that are responsible for decision making on and overseeing the management of the organization's impacts."),
                    ("c", "Describe the composition of the highest governance body and its committees by: executive and non-executive members; independence; tenure; number and nature of other significant positions and commitments held by each member; gender; under-represented social groups; competencies relevant to the impacts; and stakeholder representation."),
                ),
            ),
            Disclosure(
                "2-10",
                "Nomination and selection of the highest governance body",
                _r(
                    ("a", "Describe the nomination and selection processes for the highest governance body and its committees."),
                    ("b", "Describe the criteria used for nominating and selecting highest governance body members, including whether and how views of stakeholders (including shareholders), diversity, independence, and competencies relevant to the impacts are taken into consideration."),
                ),
            ),
            Disclosure(
                "2-11",
                "Chair of the highest governance body",
                _r(
                    ("a", "Report whether the chair of the highest governance body is also a senior executive in the organization."),
                    ("b", "If the chair is also a senior executive, explain their function within the organization's management, the reasons for this arrangement, and how conflicts of interest are prevented and mitigated."),
                ),
            ),
            Disclosure(
                "2-12",
                "Role of the highest governance body in overseeing the management of impacts",
                _r(
                    ("a", "Describe the role of the highest governance body and of senior executives in developing, approving, and updating the organization's purpose, value or mission statements, strategies, policies, and goals related to sustainable development."),
                    ("b", "Describe the role of the highest governance body in overseeing the organization's due diligence and other processes to identify and manage impacts, including whether and how it engages with stakeholders and how it considers the outcomes of these processes."),
                    ("c", "Describe the role of the highest governance body in reviewing the effectiveness of the processes described in 2-12-b, and report the frequency of this review."),
                ),
            ),
            Disclosure(
                "2-13",
                "Delegation of responsibility for managing impacts",
                _r(
                    ("a", "Describe how the highest governance body delegates responsibility for managing impacts, including whether it has appointed any senior executives with responsibility for the management of impacts and whether it has delegated responsibility to other employees."),
                    ("b", "Describe the process and frequency for senior executives or other employees to report back to the highest governance body on the management of impacts."),
                ),
            ),
            Disclosure(
                "2-14",
                "Role of the highest governance body in sustainability reporting",
                _r(
                    ("a", "Report whether the highest governance body is responsible for reviewing and approving the reported information, including the organization's material topics, and if so, describe the process for reviewing and approving the information."),
                    ("b", "If the highest governance body is not responsible for reviewing and approving the reported information, explain the reason for this."),
                ),
            ),
            Disclosure(
                "2-15",
                "Conflicts of interest",
                _r(
                    ("a", "Describe the processes for the highest governance body to ensure that conflicts of interest are prevented and mitigated."),
                    ("b", "Report whether conflicts of interest are disclosed to stakeholders, including, at a minimum, conflicts relating to cross-board membership, cross-shareholding with suppliers and other stakeholders, existence of controlling shareholders, and related parties, their relationships, transactions, and outstanding balances."),
                ),
            ),
            Disclosure(
                "2-16",
                "Communication of critical concerns",
                _r(
                    ("a", "Describe whether and how critical concerns are communicated to the highest governance body."),
                    ("b", "Report the total number and the nature of critical concerns that were communicated to the highest governance body during the reporting period."),
                ),
            ),
            Disclosure(
                "2-17",
                "Collective knowledge of the highest governance body",
                _r(
                    ("a", "Report measures taken to advance the collective knowledge, skills, and experience of the highest governance body on sustainable development."),
                ),
            ),
            Disclosure(
                "2-18",
                "Evaluation of the performance of the highest governance body",
                _r(
                    ("a", "Describe the processes for evaluating the performance of the highest governance body in overseeing the management of the organization's impacts."),
                    ("b", "Report whether the evaluations are independent or not, and the frequency of the evaluations."),
                    ("c", "Describe actions taken in response to the evaluations, including changes to the composition of the highest governance body and organizational practices."),
                ),
            ),
            Disclosure(
                "2-19",
                "Remuneration policies",
                _r(
                    ("a", "Describe the remuneration policies for members of the highest governance body and senior executives, including fixed pay and variable pay, sign-on bonuses or recruitment incentive payments, termination payments, clawbacks, and retirement benefits."),
                    ("b", "Describe how the remuneration policies for members of the highest governance body and senior executives relate to their objectives and performance in relation to the management of the organization's impacts."),
                ),
            ),
            Disclosure(
                "2-20",
                "Process to determine remuneration",
                _r(
                    ("a", "Describe the process for designing its remuneration policies and for determining remuneration, including whether independent highest governance body members or an independent remuneration committee oversees the process; how the views of stakeholders (including shareholders) are sought and taken into consideration; and whether remuneration consultants are involved and, if so, whether they are independent."),
                    ("b", "Report the results of votes of stakeholders (including shareholders) on remuneration policies and proposals, if applicable."),
                ),
            ),
            Disclosure(
                "2-21",
                "Annual total compensation ratio",
                _r(
                    ("a", "Report the ratio of the annual total compensation for the organization's highest-paid individual to the median annual total compensation for all employees (excluding the highest-paid individual)."),
                    ("b", "Report the ratio of the percentage increase in annual total compensation for the highest-paid individual to the median percentage increase in annual total compensation for all employees (excluding the highest-paid individual)."),
                    ("c", "Report contextual information necessary to understand the data and how the data has been compiled."),
                ),
            ),
            Disclosure(
                "2-22",
                "Statement on sustainable development strategy",
                _r(
                    ("a", "Report a statement from the highest governance body or most senior executive of the organization about the relevance of sustainable development to the organization and its strategy for contributing to sustainable development."),
                ),
            ),
            Disclosure(
                "2-23",
                "Policy commitments",
                _r(
                    ("a", "Describe its policy commitments for responsible business conduct, including the authoritative intergovernmental instruments referenced; whether the commitments stipulate conducting due diligence, applying the precautionary principle, and respecting human rights."),
                    ("b", "Describe its specific policy commitment to respect human rights, including the internationally recognized human rights that the commitment covers and the categories of stakeholders (including at-risk or vulnerable groups) given particular attention."),
                    ("c", "Provide links to the policy commitments if publicly available, or, if not publicly available, explain the reason."),
                    ("d", "Report the level at which each of the policy commitments was approved within the organization, including whether this is the most senior level."),
                    ("e", "Report the extent to which the policy commitments apply to the organization's activities and to its business relationships."),
                    ("f", "Describe how the policy commitments are communicated to workers, business partners, and other relevant parties."),
                ),
            ),
            Disclosure(
                "2-24",
                "Embedding policy commitments",
                _r(
                    ("a", "Describe how it embeds each of its policy commitments for responsible business conduct throughout its activities and business relationships, including how it allocates responsibility to implement the commitments, how it integrates the commitments into strategies, operational policies and procedures, how it implements its commitments with and through its business relationships, and the training it provides."),
                ),
            ),
            Disclosure(
                "2-25",
                "Processes to remediate negative impacts",
                _r(
                    ("a", "Describe its commitments to provide for or cooperate in the remediation of negative impacts that the organization identifies it has caused or contributed to."),
                    ("b", "Describe its approach to identify and address grievances, including the grievance mechanisms that the organization has established or participates in."),
                    ("c", "Describe other processes by which the organization provides for or cooperates in the remediation of negative impacts that it identifies it has caused or contributed to."),
                    ("d", "Describe how the stakeholders who are the intended users of the grievance mechanisms are involved in the design, review, operation, and improvement of these mechanisms."),
                    ("e", "Describe how the organization tracks the effectiveness of the grievance mechanisms and other remediation processes, and report examples of their effectiveness, including stakeholder feedback."),
                ),
            ),
            Disclosure(
                "2-26",
                "Mechanisms for seeking advice and raising concerns",
                _r(
                    ("a", "Describe the mechanisms for individuals to seek advice on implementing the organization's policies and practices for responsible business conduct, and to raise concerns about the organization's business conduct."),
                ),
            ),
            Disclosure(
                "2-27",
                "Compliance with laws and regulations",
                _r(
                    ("a", "Report the total number of significant instances of non-compliance with laws and regulations during the reporting period, and a breakdown by instances for which fines were incurred and instances for which non-monetary sanctions were incurred."),
                    ("b", "Report the total number and the monetary value of fines for instances of non-compliance with laws and regulations that were paid during the reporting period, broken down by fines for instances that occurred in the current reporting period and in previous reporting periods."),
                    ("c", "Describe the significant instances of non-compliance."),
                    ("d", "Describe how it has determined significant instances of non-compliance."),
                ),
            ),
            Disclosure(
                "2-28",
                "Membership associations",
                _r(
                    ("a", "Report industry associations, other membership associations, and national or international advocacy organizations in which it participates in a significant role."),
                ),
            ),
        ),
    ),
    Section(
        "4. Stakeholder engagement",
        (
            Disclosure(
                "2-29",
                "Approach to stakeholder engagement",
                _r(
                    ("a", "Describe its approach to engaging with stakeholders, including the categories of stakeholders it engages with and how they are identified, the purpose of the stakeholder engagement, and how the organization seeks to ensure meaningful engagement with stakeholders."),
                ),
            ),
            Disclosure(
                "2-30",
                "Collective bargaining agreements",
                _r(
                    ("a", "Report the percentage of total employees covered by collective bargaining agreements."),
                    ("b", "For employees not covered by collective bargaining agreements, report whether the organization determines their working conditions and terms of employment based on collective bargaining agreements that cover its other employees or based on collective bargaining agreements from other organizations."),
                ),
            ),
        ),
    ),
)
