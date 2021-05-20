import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = "GEa9xtgUssma7cLkiyLx"

# youtube video about resampling
# https://www.youtube.com/watch?v=p_Fn_BksF9k


def state_list():
    fifty_states = pd.read_html(
        'https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        print(query)
        df[abbv] = (df[abbv]-df[abbv][0]) / df[abbv][0] * 100.0
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fifty_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["United States"] = (
        df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    return df


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fifty_states3.pickle')

HPI_State_Correlation = HPI_data.corr()

TX1yr = HPI_data['TX'].resample('A', how='mean')

HPI_data['TX'].plot(ax=ax1)
TX1yr.plot(ax=ax1)

plt.legend().remove()
plt.show()
