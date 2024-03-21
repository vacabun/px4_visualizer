from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    posotion_visualizer_1 = Node(
        package='px4_visualizer',
        executable='position',
        name='position_visualizer_1',
	    output='screen',
        parameters=[{'position_topic_name':'/locate/px4_1/position'}]
    )
    ld.add_action(posotion_visualizer_1)

    posotion_visualizer_2 = Node(
        package='px4_visualizer',
        executable='position',
        name='position_visualizer_2',
	    output='screen',
        parameters=[{'position_topic_name':'/locate/px4_2/position'}]
    )
    ld.add_action(posotion_visualizer_2)
    posotion_visualizer_3 = Node(
        package='px4_visualizer',
        executable='position',
        name='position_visualizer_3',
	    output='screen',
        parameters=[{'position_topic_name':'/locate/px4_3/position'}]
    )
    ld.add_action(posotion_visualizer_3)

    posotion_visualizer_4 = Node(
        package='px4_visualizer',
        executable='position',
        name='position_visualizer_4',
	    output='screen',
        parameters=[{'position_topic_name':'/locate/px4_4/position'}]
    )
    ld.add_action(posotion_visualizer_4)

    posotion_visualizer_5 = Node(
        package='px4_visualizer',
        executable='position',
        name='position_visualizer_5',
	    output='screen',
        parameters=[{'position_topic_name':'/locate/px4_5/position'}]
    )
    ld.add_action(posotion_visualizer_5)
    return ld