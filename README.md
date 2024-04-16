<p align="center">
<img src="assets/camofire_logo_text.png" width="800"/>
</p>
<h3 align="center">An interactive interface for machine learning queue selection integrations</h3>
<h1></h1>

### Technologies Used
<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>   
<a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/></a>
<a href="https://streamlit.io" target="_blank" rel="noreferrer"><img src="assets/streamlit-original.svg" width="36" height="36" alt="rlang" /></a>
</p>

## Setup
1. Install streamlit

```bash
pip install streamlit
```

2. Run the application from the terminal

```bash
streamlit run CamofireDashboard.py
```

3. Alternatively, if you want to set up an environment you can create one and then run the previous commands

```bash
python3 -m venv env && source ./env/bin/activate
pip install streamlit
streamlit run CamofireDashboard.py 
```

## Flow of the Code (A Crash Course)
> This user interface is stateful, meaning a lot of values require Streamlit's "session_state" to run with user interaction
> Any variable beginning with "state" has this set early in the code

To start, the interface takes in a csv input.  Streamlit does support direct integration with a dataframe or database directly if that is preferred.

Once the csv is imported, minor data preperation and utility configuration is done to allow calculations within python, but output to be shown in terms of metrics such as USD and percent.

Session state variables are instantiated as a baseline, the header is formed, and the interface is shown with an editable dataframe.  A line of code to detect session state changes is where the dynamic dataframe shines.

```python
if state.stateful_df is not None:
```  

Buttons are set up within the header, so the prior formed header is then filled with button options and position can be changed from the header columns in this line of code:

```python
st.columns([.5,.25, 1.5,.25,.25,.41]) 
```

Finally, dynamic metrics are printed out.  You may see empty metrics and the "align_buttons()" function.  These are used in place of html formatting for ease, but in depth customization can be done to align widgets and format the webpage in the future.

Included in the customization there is a config.toml file which is used to change the theme and an assets folder with the necessary logos.

## So What Can it Do?
The dashboard primarily serves as a hub for the machine learning predictions.  It outputs several columns of data that can be sorted and adjusted.

Multiple buttons are there to allow the table to be reset to the original predict state, the first 80 recommended items to be automatically selected, and an export for items selected only.  If you hover over the corner of the table you can download the whole table regardless of selection.  

A date selection is present, but is currently a place holder for future integartion with multiple day prediction.  A set of radio buttons is also added to adjust model prediction priorty for queue rankings. (e.g., If you prioritize margin, you can have the items in order by highest margin rank)

The metrics at the bottom of the page are dyanmic, meaning that they will change as you select items in the table.  It will tell you how many items are selected as well as important numbers such as cost, revenue, margin, etc.


## Improvements / Unused Code
As mentioned previously Streamlit does allow greater direct integration with the database directly.  This is something that could be explored in the future to streamline the queuing process and reduce bloat and computation complexity through advanced dynamic queuing within a database.

A button is included in commented out code to allow for metric calculation to be done manually rather than dynamically.  Should computation time become long for any reason, this could provide a better user experience or be used for database querying for multiple day predictions.

Error code is also commented out.  Rather than for future use, it can be a quality feature should a set queue number ever be set to ensure too many itmes are not queued.

## Credits
This interface was created as a collaboration of the E-Commerce Camofire team at the University of Central Florida for the Master of Science in Data Analytics program.
