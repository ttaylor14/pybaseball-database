# https://rstudio-pubs-static.s3.amazonaws.com/462182_b61971e803a845dc82c907f804da09d8.html

# R analysis of Statcast Plate Data

library(ggplot2)
library(dplyr)
library(stringr)


Halladay<-read.csv("~/Documents/Halladay Data.csv")

#Assign Outcomes to Swings
Halladay<-mutate(Halladay,
                 Foul_Ball=str_detect(description, "foul"),
                 Hit_Into_Play=str_detect(description, "hit"),
                 Swinging_Miss=str_detect(description, "swinging"),
                 Swing=Foul_Ball|Hit_Into_Play|Swinging_Miss)

#Define Strike Zone
TopStrikeZone <- 3.5
BotStrikeZone <- 1.5
LeftStrikeZone <- -0.85
RightStrikeZone <- 0.85
StrikeZone <- data.frame(
  x=c(LeftStrikeZone, LeftStrikeZone, RightStrikeZone, RightStrikeZone, LeftStrikeZone),
  y=c(BotStrikeZone, TopStrikeZone, TopStrikeZone, BotStrikeZone, BotStrikeZone))



ggplot(Halladay, aes(plate_x,plate_z,color=Swinging_Miss))+
  geom_point(alpha=.45)+
  facet_wrap(~pitch_type,ncol = 2)+
  facet_wrap(~ pitch_type, ncol=2) +
  scale_colour_manual(values = c("gray50", "blue2"),
                      guide = guide_legend(title = "Swing Outcome"),
                      labels=c("Contact","Miss")) +
  theme(strip.text = element_text(size = rel(1.2),hjust=0.5,color = "black"))+
  ggtitle("Roy Halladay Opponent Swing Outcomes by Pitch Type 
for 2010 MLB Season (As Seen from Catcher's Point of View)")+
  theme(plot.title = element_text(hjust = 0.5))+
  labs(y="Vertical Location", x="Horizontal Location", caption="Source:Baseball Savant")+
  theme(axis.title.y = element_text(angle=0, vjust = .5))+
  xlim(-2, 2) + ylim(-0.5, 5)+
  geom_path(aes(x,y),data = StrikeZone,lwd=1,col="black")




"""

The intention of this visualization is to provide insight into Roy Halladay’s 2010 Cy Young Award season. Specifically, I wanted to breakdown how hitters fared when swinging at his pitches. A lot of information about the effectiveness of a pitcher can be obtained by analyzing where different types of pitches are thrown, and where batters tend to swing and miss at the ball.

The data used has been gathered from Baseball Savant, which provides PITCHf/x and Statcast data for every MLB game back to 2008. PITCHf/x, a tool that provides a detailed analysis of every pitch thrown, specifies the exact location of these pitches in a Cartesian coordinate system and the type of pitch thrown. I compiled a spreadsheet that contained each pitch that opponents swung at during Roy Halladay’s 2010 season (1,739 in total), and charted it in a scatterplot. This produced four plots, as Halladay has four different pitches he can throw. The black square denotes where the average strike zone should be in the Cartesian coordinate system (according to PITCHf/x). The grey dots represent pitches that were thrown and there was contact made (in the form of a ball put into play or a foul ball), and blue dots represent pitches that were swung at and missed.

"""