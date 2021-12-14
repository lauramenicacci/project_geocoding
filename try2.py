import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


official_df = pd.read_csv('official_dataset.csv')
lat = official_df['Latitude'].unique()
lon = official_df['Longitude'].unique()
# official_df = official_df.loc[official_df['FLOW'] == 'IMPORT']
# official_df['Value'] = official_df['Value'].str.strip()
official_df['Value'] = official_df['Value'].str.replace(' ','').replace(':','0')
# print(type(official_df['Value']))
print(official_df['Value'])
official_df['Value'] = official_df['Value'].astype(float)


#fig= go.Figure()

fig.add_trace(
    px.scatter_geo(official_df,
                    lat = 'Latitude',
                    lon = 'Longitude',
                    animation_frame = 'PERIOD',
                    size_max = 55,
                    hover_name = 'REPORTER',
                    size = 'Value',
                    color = 'PARTNER')
    )

fig.update_geos(fitbounds="locations", showcountries = True)

fig.update_layout(
        updatemenus=[
        dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["true", "false"],
                    label="Import",
                    method="update"
                ),
                dict(
                    args=["false", "true"],
                    label="Export",
                    method="update"
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)




fig.show()
