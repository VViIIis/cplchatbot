{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b016e47-253e-4967-9b82-fd8168599915",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "def ask_question(question, input_type):\n",
    "\n",
    "    if input_type == \"text\":\n",
    "        response = st.text_input(question)\n",
    "    elif input_type == \"number\":\n",
    "        response = st.number_input(question)\n",
    "    elif input_type == \"select\":\n",
    "        options = st.session_state[question]\n",
    "        response = st.selectbox(question, options)\n",
    "    elif input_type == \"radio\":\n",
    "        options = st.session_state[question]\n",
    "        response = st.radio(question, options)\n",
    "    elif input_type == \"checkbox\":\n",
    "        options = st.session_state[question]\n",
    "        response = st.multiselect(question, options)\n",
    "    return response\n",
    "\n",
    "def main():\n",
    "\n",
    "    st.title(\"Contractors Pollution Liability Application\")\n",
    "\n",
    "    st.write(\"Hello, I'm here to help you complete your contractors pollution liability application. Let's get started!\")\n",
    "\n",
    "    # Section 1: General Information\n",
    "    st.header(\"Section 1: General Information\")\n",
    "    st.write(\"Please provide some general information about your company.\")\n",
    "    st.session_state[\"company_name\"] = ask_question(\"Company Name:\", \"text\")\n",
    "    st.session_state[\"address\"] = ask_question(\"Address:\", \"text\")\n",
    "    st.session_state[\"city\"] = ask_question(\"City:\", \"text\")\n",
    "    st.session_state[\"state\"] = ask_question(\"State:\", \"text\")\n",
    "    st.session_state[\"zip_code\"] = ask_question(\"Zip Code:\", \"text\")\n",
    "    st.session_state[\"phone_number\"] = ask_question(\"Phone Number:\", \"text\")\n",
    "    st.session_state[\"email\"] = ask_question(\"Email:\", \"text\")\n",
    "\n",
    "    # Section 2: Operations\n",
    "    st.header(\"Section 2: Operations\")\n",
    "    st.write(\"Please provide information about your operations.\")\n",
    "    st.session_state[\"operation_description\"] = ask_question(\"Description of Operations:\", \"text\")\n",
    "    st.session_state[\"year_started\"] = ask_question(\"Year Operations Started:\", \"number\")\n",
    "    st.session_state[\"number_of_employees\"] = ask_question(\"Number of Employees:\", \"number\")\n",
    "    st.session_state[\"annual_revenues\"] = ask_question(\"Annual Revenues:\", \"number\")\n",
    "\n",
    "    # Section 3: Insurance History\n",
    "    st.header(\"Section 3: Insurance History\")\n",
    "    st.write(\"Please provide information about your insurance history.\")\n",
    "    st.session_state[\"current_insurance_company\"] = ask_question(\"Current Insurance Company:\", \"text\")\n",
    "    st.session_state[\"policy_number\"] = ask_question(\"Policy Number:\", \"text\")\n",
    "    st.session_state[\"policy_expiration_date\"] = ask_question(\"Policy Expiration Date (MM/DD/YYYY):\", \"text\")\n",
    "\n",
    "    # Section 4: Pollution Liability Coverage\n",
    "    st.header(\"Section 4: Pollution Liability Coverage\")\n",
    "    st.write(\"Please provide information about your pollution liability coverage.\")\n",
    "    st.session_state[\"coverage_amount\"] = ask_question(\"Coverage Amount:\", \"text\")\n",
    "    st.session_state[\"retroactive_date\"] = ask_question(\"Retroactive Date (MM/DD/YYYY):\", \"text\")\n",
    "\n",
    "    # Section 5: Additional Information\n",
    "    st.header(\"Section 5: Additional Information\")\n",
    "    st.write(\"Please provide any additional information that may be relevant to your application.\")\n",
    "    st.session_state[\"additional_information\"] = ask_question(\"Additional Information:\", \"text\")\n",
    "\n",
    "    # Submit button\n",
    "    if st.button(\"Submit\"):\n",
    "        st.write(\"Thank you for submitting your application!\")\n",
    "        # TODO: Save the application data to a file or database\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    st.session_state[\"questions\"] = {}\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (dev)",
   "language": "python",
   "name": "dev"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  },
  "toc-autonumbering": true
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
