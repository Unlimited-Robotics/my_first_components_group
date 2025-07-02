FROM public.ecr.aws/unlimited-robotics/raya.core.pyraya.pyraya_base:jetsonorin.4.26.beta

ENV SHELL=/bin/bash
SHELL ["/bin/bash", "-c"]

RUN rm -rf /usr/share/keyrings/kitware*.gpg && \
    rm -rf /usr/share/keyrings/ros*.gpg && \
    curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    curl -fsSL https://apt.kitware.com/keys/kitware-archive-latest.asc | gpg --dearmor > /usr/share/keyrings/kitware-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu focal main" > /etc/apt/sources.list.d/ros2.list && \
    echo "deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu focal main" > /etc/apt/sources.list.d/kitware.list && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN sed -i '/^deb https:\/\/isaac\.download\.nvidia\.com\/isaac-ros\/ubuntu\/main focal main/s/^/#/' /etc/apt/sources.list
