# ExtractValuesFromAuditFiles
This Python script extracts sender and receiver information from a data format containing <policy_member> sections. It parses the input data, extracts sender and receiver details within each <policy_member> section, and displays the results. The values are based on Cisco CES audit_log and can be used to rebuild previously deleted policies that are focused on sender and reciever rules. 

<h2>Usage</h2>
Clone the repository to your local machine using the following command:
  
`````
git clone https://github.com/mrlukerwilkinson/policy-member-extraction.git
`````

Navigate to the cloned directory:

````
cd policy-member-extraction
````

Place your data in a text file named input.txt within the same directory.

Run the script using Python 3:

````
python3 extract.py
````

The script will display the sender and receiver information for each <policy_member> section present in the input data.

<h2>Input Data Format</h2>
The script assumes that your input data follows a specific format, where <policy_member> sections contain sender and receiver information within <sender> and <receiver> tags. If input files use different tags, update the regex with the required fields. 

<h2>How it works</h2>
<ol>
  <li>The script reads the content of the input.txt file.</li>
  <li>It uses regular expressions to find and extract sender and receiver information within each <policy_member> section.</li>
  <li>The extracted sender and receiver information are displayed on the console.</li>
</ol>

<h2>Requirements</h2>
* Python 3.x

<h2>Disclaimer</h2>
This script is provided as-is and without any warranty. It's intended to demonstrate how to extract information from a specific data format. Please make sure to understand and modify the script as needed for your use case.
