import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotnine as gg
import os

#os.getcwd()
#loading data for the lexical decision task (I am using the data from the "lexical decision" repository.)
participants = pd.read_csv("lexdec_results.csv")
#print(participants)



#Raw data
###### RTs
sns.catplot(x="frequency", y= "reaction_time", kind = "box", data=participants)
plt.suptitle("Boxplot of reaction times as a function of word frequency.")
plt.show()


sorted_g = participants.groupby(["word"])["reaction_time"].mean().sort_values()
ax = sns.boxplot(x=participants["word"], y=participants["reaction_time"], order=list(sorted_g.index), hue=participants["frequency"])
for label in ax.get_xticklabels():
    label.set_rotation(90)
#g.set_xticklabels(rotation=90, fontsize= 8)
plt.suptitle("Boxplot of reaction times as a function of particular word and its frequency.")

plt.show()


sns.pairplot(hue="frequency", vars = ("reaction_time", "accuracy"), kind = "hist", diag_kind="kde", 
            data=participants)
plt.show()

#desity plot: distribution of mean reaction times as a function of word frequency
sns.displot(participants, x="reaction_time", hue="frequency", kind="kde", fill=True)
plt.suptitle("Reaction times as a function of word frequency.")
plt.show()


#distribution of RTs as a function frequency
g= sns.catplot(x="frequency", y = "reaction_time", kind = "violin", inner=None, data=participants) #works!
sns.swarmplot(x="frequency", y = "reaction_time",color="k", size=3, data=participants, ax=g.ax) #works!
plt.suptitle("Violin plot of the reaction times as a function of word frequency.")
plt.show()



######## accuracy
#sns.catplot(x="frequency", y="accuracy", hue="frequency", kind="bar", data=participants)
ax=sns.countplot(x="accuracy", hue="frequency", data=participants) #works!
plt.suptitle("Accuracy scores as a function of word frequency.")
plt.show()




sns.scatterplot(x = participants["duration"], y = participants["reaction_time"])
plt.suptitle("Reaction times as a function of word duration.")
plt.show()

#### Aggregated data

summary = participants.groupby(by='frequency').aggregate(  # for multiple columns, use ['id', 'condition'] instead of just 'id'
    #RT = pd.NamedAgg("reaction time"),
    mean_RT=pd.NamedAgg('reaction_time', np.mean),
    std_RT=pd.NamedAgg('reaction_time', np.std),
    mean_accuracy=pd.NamedAgg('accuracy', np.median),  # lambda data: np.mean(data) - 2
    #accuracy=pd.NamedAgg("accuracy", np.count)
    # RT_HF = 
    # RT_LF =
    # RT_none =
    
    )
#print(summary)

summary.reset_index(inplace=True)


# mean reaction time as a function of word frequency
plt.figure()
plt.bar(summary["frequency"], summary["mean_RT"])
plt.errorbar(summary['frequency'], summary['mean_RT'], summary['std_RT'], fmt='.k')
plt.ylabel("Mean reaction time (ms)")
plt.suptitle("Mein reaction times as a function of word frequency.")
plt.show()
plt.close()


#summary_word.reset_index(inplace=True)
#print(summary_word)

