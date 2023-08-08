import json
import os
from typing import Any
from dotenv import load_dotenv

import requests
from pydantic import BaseModel, Field


class RevioCustomerModel(BaseModel):
    """Individual Customer Object Model"""
    customer_id: Any
    billing_address_id: Any
    service_address_id: Any
    listing_address_id: Any
    parent_customer_id: Any
    account_number: Any
    activated_date: Any
    agent_id: Any
    secondary_agent_id: Any
    close_date: Any
    created_by: Any
    created_date: Any
    updated_date: Any
    email: Any
    is_parent: Any
    registration_code: Any
    security_pin: Any
    sold_by: Any
    source: Any
    status: Any
    auto_debit_enabled: Any
    auto_debit_day: Any
    auto_debit_payment_account_id: Any
    bill_profile_id: Any
    billing_method: Any
    balance_limit: Any
    balance_limit_enabled: Any
    collection_template_id: Any
    contract_end_date: Any
    contract_start_date: Any
    cycle_date: Any
    late_fees_enabled: Any
    payment_terms_days: Any
    tax_exempt_enabled: Any
    tax_exempt_types: Any
    usage_file_enabled: Any
    usage_file_format: Any
    payment_fees_enabled: Any
    class_: str = Field(..., alias="class")
    date_of_birth: Any
    language: Any
    tax_id: Any
    suspended: Any
    suspended_date: Any
    culture: Any
    fields: Any


class RevioCustomerResponse(BaseModel):
    """JSON body response"""
    ok: bool
    has_more: bool
    record_count: int
    records: list[RevioCustomerModel]


def get_customers() -> RevioCustomerResponse:
    """Rev.io Customer endpoint"""
    api_hostname = os.getenv("REVIO_API_HOST")
    api_result = requests.get(
        url=f"{api_hostname}/v1/CustomersOptimized",
        auth=(
            os.getenv("REVIO_API_USERNAME") or "",
            os.getenv("REVIO_API_TOKEN") or "",
        ),
        timeout=30,
    )

    api_result_dict = json.loads(api_result.content)
    return RevioCustomerResponse(**api_result_dict)


if __name__ == "__main__":
    load_dotenv()
    results = get_customers()
    print(results)
